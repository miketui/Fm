#!/usr/bin/env python3
"""Discover exactly 44 target XHTML files from EPUB OPF manifest spine.

This script parses the content.opf file to extract the spine reading order,
maps spine itemrefs to manifest hrefs, and creates an initial visual audit
JSON file with metadata for each of the 44 chapter files.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List
from xml.etree import ElementTree as ET


def parse_opf_spine(opf_path: str) -> List[Dict[str, str]]:
    """Parse OPF file and extract spine items with manifest mappings.

    Args:
        opf_path: Path to content.opf file

    Returns:
        List of dicts with file metadata (path, basename, selection_reason)
    """
    if not os.path.exists(opf_path):
        raise FileNotFoundError(f"OPF file not found: {opf_path}")

    tree = ET.parse(opf_path)
    root = tree.getroot()

    # Define OPF namespace
    ns = {'opf': 'http://www.idpf.org/2007/opf'}

    # Build manifest mapping (id → href)
    manifest = {}
    for item in root.findall('.//opf:manifest/opf:item', ns):
        item_id = item.get('id')
        href = item.get('href')
        media_type = item.get('media-type')

        if item_id and href and media_type == 'application/xhtml+xml':
            manifest[item_id] = href

    # Extract spine order (itemref → id → href)
    spine_items = []
    for itemref in root.findall('.//opf:spine/opf:itemref', ns):
        idref = itemref.get('idref')

        if idref and idref in manifest:
            href = manifest[idref]

            # Skip navigation files
            if 'nav.xhtml' in href.lower() or 'toc.xhtml' in href.lower():
                continue

            # Build full path
            opf_dir = os.path.dirname(opf_path)
            full_path = os.path.normpath(os.path.join(opf_dir, href))

            # Extract basename (filename without extension)
            basename = os.path.splitext(os.path.basename(full_path))[0]

            spine_items.append({
                'file': full_path,
                'basename': basename,
                'spine_id': idref,
                'selection_reason': f'OPF spine item #{len(spine_items) + 1}',
                'issues': [],
                'computed_style_samples': {},
                'screenshots': [],
                'pdf_check': {}
            })

    return spine_items


def validate_target_count(targets: List[Dict[str, str]], expected: int = 44) -> None:
    """Validate that we found exactly the expected number of targets.

    Args:
        targets: List of target file dicts
        expected: Expected number of targets (default 44)

    Raises:
        ValueError: If count doesn't match expected
    """
    actual = len(targets)
    if actual != expected:
        raise ValueError(
            f"Expected {expected} target files but found {actual}. "
            f"Check OPF spine for missing or extra items."
        )


def write_audit_json(targets: List[Dict[str, str]], output_path: str) -> None:
    """Write initial visual audit JSON file.

    Args:
        targets: List of target file dicts
        output_path: Path to output JSON file
    """
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    audit_data = {
        'files': targets,
        'total': len(targets),
        'selection_strategy': 'OPF spine parsing',
        'selection_ambiguities': []
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(audit_data, f, indent=2, ensure_ascii=False)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Discover 44 target XHTML files from EPUB OPF spine'
    )
    parser.add_argument(
        '--opf',
        required=True,
        help='Path to content.opf file'
    )
    parser.add_argument(
        '--out',
        required=True,
        help='Output path for visual audit JSON'
    )
    parser.add_argument(
        '--expected-count',
        type=int,
        default=44,
        help='Expected number of target files (default: 44)'
    )

    args = parser.parse_args()

    try:
        # Parse OPF spine
        print(f"Parsing OPF: {args.opf}")
        targets = parse_opf_spine(args.opf)

        # Validate count
        print(f"Found {len(targets)} target files")
        validate_target_count(targets, args.expected_count)

        # Write output
        print(f"Writing audit JSON: {args.out}")
        write_audit_json(targets, args.out)

        print(f"✅ Successfully discovered {len(targets)} target files")
        print(f"   Selection strategy: OPF spine parsing")
        print(f"   Output: {args.out}")

        return 0

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
