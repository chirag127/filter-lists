# uBlock Origin Setup

## Default filter lists (enable first)

uBlock popup > Dashboard > Filter lists:

- Enable **uBlock filters** (default)
- Enable **EasyList** + **EasyPrivacy**
- Enable **AdGuard Base** + **AdGuard Tracking Protection**

These cover OISD-equivalent blocking for browser contexts.

## Custom filter subscription

Dashboard > Filter lists > Import (at bottom) > paste URL:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt
```

Click Apply changes.

## My filters (allowlist)

Dashboard > My filters > add lines:

```
@@||example.com^
```

Or paste entries from the allowlist file.

## Notes

- uBlock Origin supports full adblock syntax including `||domain^`.
- Subscribed lists auto-update based on the `Expires: 1 day` header.
