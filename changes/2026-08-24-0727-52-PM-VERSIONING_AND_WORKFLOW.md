# Versioning and workflow

## Version folders

- `versions/vX.Y.Z-name/`: immutable release or protected baseline.
- `upgrades/vX.Y.Z-development/`: mutable development line.
- `builds/core/`: generated build without Premium-only footprint dependency.
- `builds/premium/`: generated build containing the Premium/Ultimate footprint path.

## Change sequence

1. Create a dated request from `NEW_REQUEST.md`.
2. Identify the owning engine, transport packet, renderer family and card.
3. Record expected plot/request/object deltas before coding.
4. Change the smallest owning source units.
5. Rebuild deterministically; do not patch generated output.
6. Run static invariants and baseline comparisons.
7. Publish changed Pine libraries in dependency order.
8. Update pinned imports only after publication.
9. Compile and test in TradingView.
10. Freeze the accepted candidate under `versions/` with hashes and evidence.

## Release contents

Every released version should contain:

- generated master source;
- exact library sources and pinned import list;
- ordered source modules;
- manifest and SHA-256 checksums;
- static audit;
- TradingView compile record;
- chart screenshots and tested presets;
- profiler notes;
- strategy-test exports and documented assumptions;
- completed request and changelog.

## Pine grammar policy

- Global declarations begin at column zero.
- Local blocks use four spaces.
- Long calls are enclosed in parentheses and use named arguments.
- Input rows reuse deliberate `inline` keys; groups retain numerical ordering.
- Functions are defined before first use where practical.
- Global `plot*()` calls live in one final output shard.