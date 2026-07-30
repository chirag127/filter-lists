"""Strip wildcard prefix (*.) from domain entries — NextDNS raw export format."""

import sys
from pathlib import Path


def strip_wildcards(src: Path, dst: Path) -> None:
    lines = []
    for line in src.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("!") or line.startswith("#"):
            lines.append(line)
            continue
        line = line.removeprefix("*.")
        lines.append(line)
    dst.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(lines)} lines to {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: strip-wildcards.py <src> <dst>")
        sys.exit(1)
    strip_wildcards(Path(sys.argv[1]), Path(sys.argv[2]))
