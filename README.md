# filter-lists

[![Stars](https://img.shields.io/github/stars/chirag127/filter-lists?style=flat&logo=github)](https://github.com/chirag127/filter-lists/stargazers)
[![License](https://img.shields.io/github/license/chirag127/filter-lists?style=flat)](LICENSE)
[![Site](https://img.shields.io/badge/site-live-brightgreen?style=flat)](https://filter-lists.oriz.in/)

Personal DNS + browser filter lists. Custom additions that supplement OISD and AdGuard DNS defaults.

## Live Site

**https://filter-lists.oriz.in/**

## Philosophy

**Default lists first.** OISD (full) + AdGuard DNS Filter cover ~99% of blocking.
This repo contains **only the custom entries not in those defaults**.

### Enable these defaults everywhere first

| List | URL |
|------|-----|
| OISD Full | `https://big.oisd.nl` |
| AdGuard DNS Filter | `https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt` |

Then subscribe to the custom list below.

## Subscription URLs

| Format | URL | Compatible with |
|--------|-----|-----------------|
| Adblock syntax | `https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt` | AdGuard (all), uBlock Origin, Pi-hole v6 |
| Plain domains | `https://raw.githubusercontent.com/chirag127/filter-lists/main/output/domains.txt` | NextDNS custom, most resolvers |
| Hosts file | `https://raw.githubusercontent.com/chirag127/filter-lists/main/output/hosts.txt` | /etc/hosts, Pi-hole, AdGuard Home |

## Custom allowlist

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/custom/allowlist/global.txt
```

## Repository structure

```
filter-lists/
├── custom/
│   ├── blocklist/
│   │   ├── ads.txt          — ad loaders, bid SDKs
│   │   ├── analytics.txt    — crash reporters, analytics
│   │   ├── microsoft.txt    — Microsoft/Xbox telemetry
│   │   ├── misc.txt         — remaining entries
│   │   ├── mobile.txt       — mobile-specific trackers (incl. Xiaomi/MIUI)
│   │   ├── paywall.txt      — paywall engines
│   │   └── social.txt       — Facebook, consent banners
│   └── allowlist/
│       └── global.txt       — always-allow list
├── nextdns/
│   └── config/              — sanitized NextDNS profile exports (6 profiles)
│       └── README.md        — import instructions
├── output/                  — subscribe to these URLs (generated)
│   ├── adblock.txt
│   ├── domains.txt
│   └── hosts.txt
├── docs/                    — per-platform setup guides
│   ├── nextdns.md
│   ├── adguard-dns.md
│   ├── adguard-home.md
│   ├── adguard-extension.md
│   ├── ublock-origin.md
│   └── pihole.md
└── scripts/
    ├── build.py             — regenerate output/ from custom/
    └── strip-wildcards.py   — strip *. prefix from NextDNS raw export format
```

## Regenerating output/

```bash
python scripts/build.py
```

Run after editing any file in `custom/blocklist/`. Commit the updated `output/` files together.

## Setup guides

- [NextDNS](docs/nextdns.md)
- [AdGuard DNS](docs/adguard-dns.md)
- [AdGuard Home](docs/adguard-home.md)
- [AdGuard Extension](docs/adguard-extension.md)
- [uBlock Origin](docs/ublock-origin.md)
- [Pi-hole](docs/pihole.md)

## License

MIT
