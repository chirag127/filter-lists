# Pi-hole Setup

## Default lists (enable first)

Pi-hole admin > Adlists > add URLs:

- OISD Full: `https://big.oisd.nl`
- AdGuard DNS filter: `https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt`

Run `pihole -g` to update gravity after adding.

## Custom blocklist

Pi-hole admin > Adlists > Add:

- Comment: `chirag127 custom`
- Address:
  ```
  https://raw.githubusercontent.com/chirag127/filter-lists/main/output/hosts.txt
  ```

Or use plain domains format (Pi-hole v6+):

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/output/domains.txt
```

Run `pihole -g` to apply.

## Custom allowlist

Pi-hole admin > Domains > Allowlist > add domains individually, or via CLI:

```bash
pihole --white-list example.com
```

## Notes

- Hosts format (`0.0.0.0 domain`) is the most compatible format for Pi-hole.
- Pi-hole v6+ also supports plain domain lists via adlists.
