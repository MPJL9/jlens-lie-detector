"""Shared helpers: model registry, device, model + lens loading, chat
formatting with token-span bookkeeping, Yes/No token sets.

Every stage imports from here so that the chat template, the answer-token
sets and the layer indexing are defined exactly once.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field

import torch

logger = logging.getLogger("exp0")

# ---------------------------------------------------------------------------
# model registry: HF id + published lens location (neuronpedia/jacobian-lens)
# ---------------------------------------------------------------------------
LENS_REPO = "neuronpedia/jacobian-lens"

MODELS = {
    "gemma-3-4b-it": dict(
        hf="google/gemma-3-4b-it",
        lens_file="gemma-3-4b-it/jlens/Salesforce-wikitext/gemma-3-4b-it_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={}),
    "gemma-3-12b-it": dict(
        hf="google/gemma-3-12b-it",
        lens_file="gemma-3-12b-it/jlens/Salesforce-wikitext/gemma-3-12b-it_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={}),
    "gemma-3-1b-it": dict(
        hf="google/gemma-3-1b-it",
        lens_file="gemma-3-1b-it/jlens/Salesforce-wikitext/gemma-3-1b-it_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={}),
    # ~55GB bf16 weights: needs an A100-80GB or H200;
    # does NOT fit the L40S-48GB or A100-40GB cards
    "gemma-3-27b-it": dict(
        hf="google/gemma-3-27b-it",
        lens_file="gemma-3-27b-it/jlens/Salesforce-wikitext/gemma-3-27b-it_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={}),
    # ungated chat model with a published lens — local dry runs
    "qwen3-1.7b": dict(
        hf="Qwen/Qwen3-1.7B",
        lens_file="qwen3-1.7b/jlens/Salesforce-wikitext/Qwen3-1.7B_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={"enable_thinking": False}),
    "qwen3.6-27b": dict(
        hf="Qwen/Qwen3.6-27B",
        lens_file="qwen3.6-27b/jlens/Salesforce-wikitext/Qwen3.6-27B_jacobian_lens_n1000.pt",
        lens_rev="qwen-n1000", chat=True, chat_kwargs={"enable_thinking": False}),
    # smaller instruct Qwens (lens filenames verified on the hub 2026-08-26)
    "qwen3-14b": dict(
        hf="Qwen/Qwen3-14B",
        lens_file="qwen3-14b/jlens/Salesforce-wikitext/Qwen3-14B_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={"enable_thinking": False}),
    "qwen3-8b": dict(
        hf="Qwen/Qwen3-8B",
        lens_file="qwen3-8b/jlens/Salesforce-wikitext/Qwen3-8B_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={"enable_thinking": False}),
    # harmony-format reasoning model: generation emits an "results" channel
    # (chain of thought) before the "final" channel; decode_response() strips
    # it, and build_transcripts bumps token budgets when spec has harmony=True
    "gpt-oss-20b": dict(
        hf="openai/gpt-oss-20b",
        lens_file="gpt-oss-20b/jlens/Salesforce-wikitext/gpt-oss-20b_jacobian_lens.pt",
        lens_rev="main", chat=True, chat_kwargs={"reasoning_effort": "low"},
        harmony=True),
    # not a chat model — code-path smoke test only (plain "User:/Assistant:" format)
    "gpt2": dict(
        hf="gpt2",
        lens_file="gpt2-small/jlens/Salesforce-wikitext/gpt2_jacobian_lens.pt",
        lens_rev="main", chat=False, chat_kwargs={}),
}


def model_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def pick_device(pref: str | None = None) -> torch.device:
    if pref:
        return torch.device(pref)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def pick_dtype(device: torch.device) -> torch.dtype:
    # Gemma overflows in fp16; bf16 works on CUDA and on Apple-silicon MPS.
    return torch.float32 if device.type == "cpu" else torch.bfloat16


def gpu_sanity():
    """Slurm allocated a GPU but torch can't see it -> hard fail (cluster doc §4)."""
    if os.environ.get("SLURM_JOB_ID") and not torch.cuda.is_available():
        sys.exit("FATAL: GPU allocated but torch.cuda.is_available()==False")


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------
@dataclass
class Loaded:
    name: str
    spec: dict
    hf_model: torch.nn.Module
    tokenizer: object
    lens_model: object          # jlens.HFLensModel
    device: torch.device
    dtype: torch.dtype
    n_layers: int = 0
    d_model: int = 0


def load_model(name: str, device: str | None = None, attn: str | None = None) -> Loaded:
    import transformers
    import jlens

    spec = MODELS[name]
    dev = pick_device(device)
    dt = pick_dtype(dev)
    logger.info("loading %s on %s (%s)", spec["hf"], dev, dt)
    kw = {}
    if attn:
        kw["attn_implementation"] = attn
    # low_cpu_mem_usage: 27B weights (~55GB bf16) must not be materialized twice
    # in CPU RAM before .to(device) — slurm jobs only request 48-120GB
    hf = transformers.AutoModelForCausalLM.from_pretrained(
        spec["hf"], dtype=dt, low_cpu_mem_usage=True, **kw)
    hf.to(dev).eval()
    tok = transformers.AutoTokenizer.from_pretrained(spec["hf"])
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    lm = jlens.from_hf(hf, tok)
    L = Loaded(name=name, spec=spec, hf_model=hf, tokenizer=tok, lens_model=lm,
               device=dev, dtype=dt, n_layers=lm.n_layers, d_model=lm.d_model)
    logger.info("loaded: %s", lm)
    return L


def load_lens(name: str):
    import jlens
    spec = MODELS[name]
    lens = jlens.JacobianLens.from_pretrained(
        LENS_REPO, filename=spec["lens_file"], revision=spec["lens_rev"])
    logger.info("lens: %s", lens)
    return lens


# ---------------------------------------------------------------------------
# Yes / No token sets
# ---------------------------------------------------------------------------
YES_SURFACES = ["Yes", " Yes", "yes", " yes", "YES", " YES"]
NO_SURFACES = ["No", " No", "no", " no", "NO", " NO"]


def single_token_ids(tok, surfaces: list[str]) -> dict[str, int]:
    """{surface: id} for surfaces that tokenize to exactly one token."""
    out = {}
    for s in surfaces:
        ids = tok.encode(s, add_special_tokens=False)
        if len(ids) == 1 and ids[0] not in out.values():
            out[s] = ids[0]
    return out


def yes_no_sets(tok) -> dict:
    y = single_token_ids(tok, YES_SURFACES)
    n = single_token_ids(tok, NO_SURFACES)
    assert y and n, "tokenizer has no single-token Yes/No?"
    return {"yes": y, "no": n}


def classify_answer(text: str, style: str = "yesno") -> str:
    """Behavioral label of a generated self-report: yes / no / other.
    style='ab' (Q7_ab, lie-detectors-post format): A = yes-I-lied, B = no."""
    t = text.strip().lstrip("*#` \n\"'(").lower()
    if style == "ab":
        if t.startswith("a"):
            return "yes"
        if t.startswith("b"):
            return "no"
        return "other"
    if t.startswith("yes"):
        return "yes"
    if t.startswith("no"):
        return "no"
    return "other"


# ---------------------------------------------------------------------------
# chat formatting with span bookkeeping
# ---------------------------------------------------------------------------
@dataclass
class Seq:
    """A tokenized sequence plus the char/token spans of its parts."""
    text: str
    ids: list[int]
    offsets: list[tuple[int, int]]
    segments: list[dict] = field(default_factory=list)   # {name,start,end} token spans (end excl.)

    def span_tokens(self, cs: int, ce: int) -> tuple[int, int]:
        """token [start,end) covering char span [cs,ce)."""
        idx = [i for i, (a, b) in enumerate(self.offsets) if b > cs and a < ce and b > a]
        if not idx:
            raise ValueError(f"no tokens cover chars {cs}:{ce}")
        return idx[0], idx[-1] + 1


def render_chat(L: Loaded, messages: list[dict], add_generation_prompt: bool) -> str:
    tok = L.tokenizer
    if L.spec["chat"]:
        return tok.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=add_generation_prompt,
            **L.spec["chat_kwargs"])
    # plain fallback for non-chat models (smoke tests)
    role = {"user": "User", "assistant": "Assistant", "system": "System"}
    s = "".join(f"{role[m['role']]}: {m['content'].strip()}\n" for m in messages)
    if add_generation_prompt:
        s += "Assistant:"
    return s


def tokenize_with_offsets(L: Loaded, text: str) -> Seq:
    enc = L.tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
    return Seq(text=text, ids=list(enc["input_ids"]),
               offsets=[tuple(o) for o in enc["offset_mapping"]])


def decode_response(L: Loaded, new_ids: list[int]) -> str:
    """Decode generated ids to the VISIBLE response text.

    Harmony-format models (spec harmony=True, e.g. gpt-oss) emit
    `<|channel|>analysis<|message|>…chain of thought…` before
    `<|channel|>final<|message|>…answer…`; skip_special_tokens would silently
    concatenate the two. Return only the final-channel text; if generation
    ended before a final channel appeared (budget exhausted mid-analysis),
    return "" so the caller's parse fails visibly instead of reading CoT.
    """
    if L.spec.get("harmony"):
        raw = L.tokenizer.decode(new_ids, skip_special_tokens=False)
        if "<|channel|>final<|message|>" not in raw:
            return ""
        raw = raw.rsplit("<|channel|>final<|message|>", 1)[1]
        for stop in ("<|return|>", "<|end|>", "<|endoftext|>", "<|start|>"):
            raw = raw.split(stop, 1)[0]
        return raw.strip()
    return L.tokenizer.decode(new_ids, skip_special_tokens=True)


def build_followup(L: Loaded, user_prompt: str, response: str, self_q: str,
                   system: str | None = None,
                   prior_turns: list[dict] | None = None) -> Seq:
    """Tokenize  [user prompt] [assistant response] [user self-report q] + gen prompt
    and mark segments: user_prompt, response, self_q, gen_prompt.

    prior_turns (campaign 2, MASK doubling_down): earlier user/assistant turns
    inserted between the system prompt and the final pressured user turn; the
    `user_prompt` segment always names the LAST user turn before the response.

    Chat templates may trim message content, so spans are located by searching
    the rendered text for the stripped content, left to right."""
    msgs = ([{"role": "system", "content": system}] if system else []) +            list(prior_turns or []) +            [{"role": "user", "content": user_prompt},
            {"role": "assistant", "content": response},
            {"role": "user", "content": self_q}]
    text = render_chat(L, msgs, add_generation_prompt=True)
    seq = tokenize_with_offsets(L, text)
    cursor = 0
    # None-named parts (prior turns) advance the cursor without recording a segment
    parts = ([("system", system)] if system else []) +             [(None, m["content"]) for m in (prior_turns or [])] +             [("user_prompt", user_prompt), ("response", response), ("self_q", self_q)]
    for name, content in parts:
        c = content.strip()
        cs = text.find(c, cursor)
        if cs < 0:
            raise ValueError(f"could not locate {name!r} in rendered chat text")
        ce = cs + len(c)
        if name is not None:
            ts, te = seq.span_tokens(cs, ce)
            seq.segments.append({"name": name, "start": ts, "end": te})
        cursor = ce
    # everything after the self-report question up to the end = template tail + gen prompt
    last = seq.segments[-1]["end"]
    seq.segments.append({"name": "gen_prompt", "start": last, "end": len(seq.ids)})
    return seq


def seg(seq_or_segments, name: str) -> dict:
    segs = seq_or_segments.segments if hasattr(seq_or_segments, "segments") else seq_or_segments
    for s in segs:
        if s["name"] == name:
            return s
    raise KeyError(name)


# ---------------------------------------------------------------------------
# generation
# ---------------------------------------------------------------------------
@torch.no_grad()
def generate(L: Loaded, ids: list[int], max_new_tokens: int,
             temperature: float = 0.0, seed: int | None = None) -> list[int]:
    """Greedy (temperature=0) or sampled continuation; returns new ids (EOS stripped)."""
    inp = torch.tensor([ids], device=L.device)
    kw = dict(do_sample=False) if temperature <= 0 else         dict(do_sample=True, temperature=temperature, top_p=0.95)
    if seed is not None:
        torch.manual_seed(seed)
    out = L.hf_model.generate(
        input_ids=inp, attention_mask=torch.ones_like(inp),
        max_new_tokens=max_new_tokens, pad_token_id=L.tokenizer.pad_token_id, **kw)
    new = out[0, inp.shape[1]:].tolist()
    eos = set(L.hf_model.generation_config.eos_token_id or []) \
        if isinstance(L.hf_model.generation_config.eos_token_id, list) \
        else {L.hf_model.generation_config.eos_token_id}
    eos |= {L.tokenizer.eos_token_id}
    cut = [i for i, t in enumerate(new) if t in eos]
    return new[:cut[0]] if cut else new


# ---------------------------------------------------------------------------
# io
# ---------------------------------------------------------------------------
def read_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def write_jsonl(path, rows):
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.getLogger("transformers").setLevel(logging.WARNING)
