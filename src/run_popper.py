#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


# -----------------------------
# Make sure *your vendored* Popper is importable
# -----------------------------
def ensure_vendored_popper_on_path() -> None:
    """
    Your traceback shows Popper is vendored at:
      <project>/src/popper/lib/popper/...
    Add <project>/src/popper/lib to sys.path if needed.
    """
    here = Path(__file__).resolve()
    project_root = here.parents[1]  # .../Project/ReversingSudoku
    vendored = project_root / "src" / "popper" / "lib"
    if vendored.exists():
        sys.path.insert(0, str(vendored))


# -----------------------------
# Helpers
# -----------------------------
def die(msg: str, code: int = 2) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
    raise SystemExit(code)


def ensure_file(p: Path, label: str) -> None:
    if not p.exists() or not p.is_file():
        die(f"{label} not found: {p}")


def run_cmd(cmd: Sequence[str], *, timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            list(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError:
        die(f"Command not found: {cmd[0]}")


def parse_body_preds_from_bias(bias_path: Path) -> List[Tuple[str, int]]:
    """
    Extract body_pred(name,arity). from bias.pl.
    Works even if there are comments and spaces.
    """
    text = bias_path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"%[^\n]*", "", text)  # remove Prolog line comments

    pat = re.compile(r"\bbody_pred\s*\(\s*([a-z][a-zA-Z0-9_]*)\s*,\s*([0-9]+)\s*\)\s*\.", re.MULTILINE)
    preds = [(m.group(1), int(m.group(2))) for m in pat.finditer(text)]

    # unique but stable order
    seen = set()
    out: List[Tuple[str, int]] = []
    for n, a in preds:
        if (n, a) not in seen:
            seen.add((n, a))
            out.append((n, a))
    return out


def make_popper_input_dir(bk: Path, bias: Path, exs: Path, *, keep_dir: Optional[Path]) -> Path:
    """
    Popper expects a directory containing bk.pl, bias.pl, exs.pl.
    We'll copy your files into that format.
    """
    if keep_dir is not None:
        keep_dir.mkdir(parents=True, exist_ok=True)
        out_dir = keep_dir
    else:
        out_dir = Path(tempfile.mkdtemp(prefix="popper_input_"))

    shutil.copyfile(bk, out_dir / "bk.pl")
    shutil.copyfile(bias, out_dir / "bias.pl")
    shutil.copyfile(exs, out_dir / "exs.pl")
    return out_dir


def _var_name(i: int) -> str:
    # 0->S, 1->T, 2->U ... (good enough)
    alphabet = "STUVWXYZABCDEFGHIJKLMPQR"
    return alphabet[i] if 0 <= i < len(alphabet) else f"V{i}"

def _lit_to_prolog(lit) -> str:
    # lit has .predicate and .arguments in your Popper fork
    pred = getattr(lit, "predicate", None)
    args = getattr(lit, "arguments", None)
    if pred is None or args is None:
        return str(lit)
    # arguments are ints representing variable ids
    arg_str = ", ".join(_var_name(a) if isinstance(a, int) else str(a) for a in args)
    return f"{pred}({arg_str})"

def prog_to_str(prog: object) -> str:
    if prog is None:
        return ""

    # Already a Prolog-ish string
    if isinstance(prog, str):
        return prog.strip()

    # New: Popper in your repo returns frozenset/set of rules
    if isinstance(prog, (set, frozenset)):
        clauses = []
        for rule in prog:
            # rule is typically (HeadLiteral, BodySet)
            if isinstance(rule, tuple) and len(rule) == 2:
                head, body = rule
                head_s = _lit_to_prolog(head)

                if isinstance(body, (set, frozenset)) and len(body) > 0:
                    body_s = ", ".join(_lit_to_prolog(b) for b in body)
                    clauses.append(f"{head_s} :- {body_s}.")
                else:
                    clauses.append(f"{head_s}.")
            else:
                clauses.append(str(rule))
        return "\n".join(clauses).strip()

    # List/tuple of clauses fallback
    if isinstance(prog, (list, tuple)):
        return "\n".join(str(x).strip() for x in prog if str(x).strip()).strip()

    return str(prog).strip()



def rename_pred_calls(prog: str, old: str, new: str) -> str:
    # Replace occurrences like old( ... with new(
    return re.sub(rf"\b{re.escape(old)}\s*\(", f"{new}(", prog)


# -----------------------------
# SWI-Prolog evaluation (optional)
# -----------------------------
def eval_with_swi(*, bk: Path, exs: Path, prog: str, head_pred: str, timeout_s: int = 30) -> None:
    if not prog.strip():
        print("\n[WARN] Empty hypothesis; skipping SWI evaluation.")
        return

    hyp_pred = f"hyp_{head_pred}"
    renamed = rename_pred_calls(prog, head_pred, hyp_pred)

    # Normalize: ensure every clause ends with "."
    lines = []
    for line in renamed.splitlines():
        s = line.strip()
        if not s:
            continue
        if not s.endswith("."):
            s += "."
        lines.append(s)
    hyp_program = "\n".join(lines) + "\n"

    prolog_src = f"""
:- initialization(run).

:- ['{bk.as_posix()}'].
:- ['{exs.as_posix()}'].

{hyp_program}

holds(G) :- call(G), !.
holds(_G) :- fail.

run :-
  findall(S, pos({head_pred}(S)), Ps),
  findall(S, neg({head_pred}(S)), Ns),
  length(Ps, P),
  length(Ns, N),

  findall(S, (member(S, Ps), holds({hyp_pred}(S))), TPs),
  findall(S, (member(S, Ps), \\+ holds({hyp_pred}(S))), FNs),

  findall(S, (member(S, Ns), holds({hyp_pred}(S))), FPs),
  findall(S, (member(S, Ns), \\+ holds({hyp_pred}(S))), TNs),

  length(TPs, TP), length(FNs, FN), length(FPs, FP), length(TNs, TN),

  format("=== SWI CONFUSION MATRIX ===~n"),
  format("P=~w N=~w TP=~w FN=~w FP=~w TN=~w~n", [P,N,TP,FN,FP,TN]),

  ( FPs = [FirstFP|_] ->
      format("First FP example:~n"),
      write_term(FirstFP, [quoted(false)]), nl
  ; true ),

  ( FNs = [FirstFN|_] ->
      format("First FN example:~n"),
      write_term(FirstFN, [quoted(false)]), nl
  ; true ),

  halt.
"""

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".pl", encoding="utf-8") as f:
        tmp_pl = Path(f.name)
        f.write(prolog_src)

    try:
        cp = run_cmd(["swipl", "-q", "-s", str(tmp_pl)], timeout=timeout_s)
        if cp.returncode != 0:
            print(cp.stdout)
            print(cp.stderr, file=sys.stderr)
            die(f"SWI-Prolog evaluation failed (exit={cp.returncode}).")
        print("\n" + cp.stdout.rstrip())
    finally:
        try:
            tmp_pl.unlink(missing_ok=True)
        except Exception:
            pass


# -----------------------------
# Popper run (your vendored API)
# -----------------------------
def run_popper(
    input_dir: Path,
    *,
    timeout: int,
    force_recall: Optional[int],
) -> Tuple[object, object, object]:
    """
    Works with your vendored Popper:
      from popper.util import Settings
      from popper.loop import learn_solution
    Important: do NOT overwrite settings.stats (it's a Stats object in your fork).
    """
    ensure_vendored_popper_on_path()
    try:
        from popper.util import Settings  # type: ignore
        from popper.loop import learn_solution  # type: ignore
    except Exception as e:
        die(f"Could not import your vendored Popper. Import error: {e}")

    settings = Settings(kbpath=str(input_dir))

    # Safe: timeout is an int in your fork (your earlier logs show it)
    if hasattr(settings, "timeout"):
        settings.timeout = int(timeout)

    # Safe: recall dict
    if force_recall is not None:
        body_preds = parse_body_preds_from_bias(input_dir / "bias.pl")
        settings.recall = {(n, a): int(force_recall) for (n, a) in body_preds}
        print(f"Forced settings.recall = {settings.recall}")
        print(f"type(settings.recall) = {type(settings.recall)}")
        print(f"settings.recall currently = {settings.recall}")

    # Learn
    prog, score, stats_obj = learn_solution(settings)
    return prog, score, stats_obj


# -----------------------------
# Main
# -----------------------------
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--debug", action="store_true", help="Enable Popper debug output (if supported).")
    ap.add_argument("--bk", type=Path, required=True)
    ap.add_argument("--bias", type=Path, required=True)
    ap.add_argument("--exs", type=Path, required=True)
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--force-recall", type=int, default=None)
    ap.add_argument("--keep-input-dir", type=Path, default=None)
    ap.add_argument("--head-pred", type=str, default="valid_sudoku")
    ap.add_argument("--skip-swi", action="store_true")
    args = ap.parse_args()

    ensure_file(args.bk, "BK")
    ensure_file(args.bias, "Bias")
    ensure_file(args.exs, "Examples")

    input_dir = make_popper_input_dir(args.bk, args.bias, args.exs, keep_dir=args.keep_input_dir)

    try:
        prog, score, stats_obj = run_popper(
            input_dir,
            timeout=args.timeout,
            force_recall=args.force_recall,
        )

        prog_str = prog_to_str(prog)

        print("DONE")
        print("Score:", score)
        print("Stats:", stats_obj)
        # stats_obj in your fork prints a dict-like durations; leave it as-is

        print("\nLearned program:")
        print(prog_str if prog_str else "<empty>")
        print("repr(hyp) =", repr(prog_str))
        print("type(hyp) =", type(prog_str))

        if not args.skip_swi:
            eval_with_swi(bk=args.bk, exs=args.exs, prog=prog_str, head_pred=args.head_pred)

    finally:
        if args.keep_input_dir is None:
            shutil.rmtree(input_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
