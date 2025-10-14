#!/usr/bin/env python3
"""Compare XHTML files to guarantee text fidelity after structural edits."""

from __future__ import annotations

import argparse
import difflib
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Sequence


class XHTMLTextExtractor(HTMLParser):
    """Extract raw text tokens from XHTML without altering punctuation."""

    def __init__(self) -> None:
        super().__init__()
        self.tokens: List[str] = []

    def handle_data(self, data: str) -> None:  # noqa: D401 - HTMLParser hook
        parts = data.split()
        if parts:
            self.tokens.extend(parts)

    def get_tokens(self) -> List[str]:
        return self.tokens


def tokenise(path: Path) -> List[str]:
    extractor = XHTMLTextExtractor()
    try:
        extractor.feed(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:  # pragma: no cover - diagnostic path
        raise RuntimeError(f"Failed to decode {path}") from exc
    extractor.close()
    return extractor.get_tokens()


def collect_pairs(baseline_dir: Path, modified_dir: Path) -> Dict[Path, Path]:
    pairs: Dict[Path, Path] = {}
    for baseline_file in sorted(baseline_dir.glob("*.xhtml")):
        relative = baseline_file.name
        modified_file = modified_dir / relative
        if not modified_file.exists():
            raise FileNotFoundError(f"Missing modified file for {relative}")
        pairs[baseline_file] = modified_file
    return pairs


def unified_diff_tokens(a_tokens: Sequence[str], b_tokens: Sequence[str], fromfile: str, tofile: str) -> str:
    diff = difflib.unified_diff(
        [f"{token}\n" for token in a_tokens],
        [f"{token}\n" for token in b_tokens],
        fromfile=fromfile,
        tofile=tofile,
        lineterm="",
    )
    return "\n".join(diff)


def generate_report(pairs: Dict[Path, Path], report_path: Path | None) -> int:
    mismatches = 0
    report_lines: List[str] = []

    for baseline_file, modified_file in pairs.items():
        baseline_tokens = tokenise(baseline_file)
        modified_tokens = tokenise(modified_file)
        baseline_count = len(baseline_tokens)
        modified_count = len(modified_tokens)
        status = "MATCH" if baseline_tokens == modified_tokens else "MISMATCH"

        summary = (
            f"{baseline_file.name}: {status}\n"
            f"  baseline words: {baseline_count}\n"
            f"  modified words: {modified_count}\n"
        )
        report_lines.append(summary)

        if status == "MISMATCH":
            mismatches += 1
            diff_text = unified_diff_tokens(
                baseline_tokens,
                modified_tokens,
                fromfile=f"baseline/{baseline_file.name}",
                tofile=f"modified/{modified_file.name}",
            )
            report_lines.append(diff_text or "  (Diff suppressed: token sequences differ but diff is empty)")

    output = "\n".join(report_lines)

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(output, encoding="utf-8")

    print(output)
    return mismatches


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify XHTML text fidelity")
    parser.add_argument("--baseline", type=Path, default=Path("input/OEBPS/text"), help="Directory with original XHTML files")
    parser.add_argument("--modified", type=Path, default=Path("output/OEBPS/text"), help="Directory with edited XHTML files")
    parser.add_argument("--report", type=Path, help="Optional path to write a detailed report")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    baseline_dir: Path = args.baseline
    modified_dir: Path = args.modified

    if not baseline_dir.exists() or not modified_dir.exists():
        raise FileNotFoundError("Baseline and modified directories must both exist")

    pairs = collect_pairs(baseline_dir, modified_dir)
    mismatches = generate_report(pairs, args.report)

    if mismatches:
        print(f"\n❌  Content fidelity check failed for {mismatches} file(s).")
        return 1

    print("\n✅  All XHTML files match baseline prose.")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
