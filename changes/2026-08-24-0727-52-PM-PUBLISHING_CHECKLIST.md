# Publishing checklist

This workspace separates a reproducible local checkpoint from any external
Git or TradingView publication. Do not treat a passing local audit as proof of
TradingView compilation or runtime behavior.

## Before the first Git remote push

- Run `./tools/verify_all.sh` from the workspace root.
- Confirm `git status --short` contains only reviewed files.
- Confirm no credential, private-key, `.env`, cache, or editor-auth artifact is
  tracked.
- Decide whether the repository is private or public. A public repository will
  expose the complete strategy source and the TradingView publisher identity.
- Decide the repository-level license. Source files carry MPL-2.0 notices, but
  the workspace currently has no root `LICENSE` file.
- Configure the real commit author identity; never invent one for automation.
- Add and verify the exact remote URL before pushing.
- Create separate commits for the immutable baseline and Stage 8 tooling so the
  provenance boundary is reviewable.

## Before TradingView publication

- Publish changed libraries in dependency order with immutable version numbers.
- Verify the locally locked source bytes against the actual published library
  sources.
- Compile the master against those published versions in Pine v6.
- Record the compiler-reported plot count and resolve every warning/error.
- Test historical load, realtime updates, chart reload, and Bar Replay.
- Exercise all feature toggles and score-pool combinations.
- Measure live line, box, label, and table use on long datasets and volatile
  symbols.
- Review MTF requests for confirmed values and validate requested timeframes.
- Save evidence under `upgrades/v8.0.0-development/tests/tradingview/`.