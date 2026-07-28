"""Build output/ from custom/blocklist/ source files."""

from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "custom" / "blocklist"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

DATE = "2026-07-28"

HEADER_ADBLOCK = f"""! Title: chirag127 Custom Filter List
! Description: Custom DNS blocklist supplementing OISD + AdGuard defaults
! Homepage: https://github.com/chirag127/filter-lists
! Raw: https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt
! License: MIT
! Expires: 1 day
! Updated: {DATE}
! Note: Only contains domains NOT in OISD (full) or AdGuard DNS Filter
"""

domains = []
for src_file in sorted(SRC.glob("*.txt")):
    for line in src_file.read_text().splitlines():
        line = line.strip()
        if line.startswith("!") or not line:
            continue
        if line.startswith("||") and line.endswith("^"):
            domain = line[2:-1]
            domains.append(domain)

domains = sorted(set(domains))

# adblock.txt
lines = [HEADER_ADBLOCK.rstrip()]
for d in domains:
    lines.append(f"||{d}^")
(OUT / "adblock.txt").write_text("\n".join(lines) + "\n")

# domains.txt
header_domains = (
    f"# chirag127 Custom Filter List — plain domains\n"
    f"# Updated: {DATE}\n"
    f"# Only supplements OISD + AdGuard defaults\n"
)
(OUT / "domains.txt").write_text(header_domains + "\n".join(domains) + "\n")

# hosts.txt
header_hosts = f"# chirag127 Custom Filter List — hosts format\n# Updated: {DATE}\n"
hosts_lines = [header_hosts.rstrip()] + [f"0.0.0.0 {d}" for d in domains]
(OUT / "hosts.txt").write_text("\n".join(hosts_lines) + "\n")

print(f"Built {len(domains)} domains into output/")
