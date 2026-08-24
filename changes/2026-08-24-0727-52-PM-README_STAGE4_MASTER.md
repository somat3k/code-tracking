# PITBULL Master Library Orchestrator • Stage 4

This package settles Stages 1–4 into one orchestration model.

## Dependency tree

PB_Types/1
PB_Math/2
    ├─ PB_Performer/2
    ├─ PB_Governor/2
    ├─ PB_Router/2
    ├─ PB_Context/1
    ├─ PB_Waves/1
    ├─ PB_Structure/1
    └─ PB_Geometry/1
          └─ imports PB_Structure/1

Main imports every engine it directly presents.

## Stage 4 libraries

### PB_Structure
Owns:
- confirmed pivot state
- high/low history required by geometry
- alternating A/B/C pivot state
- BOS
- CHoCH
- liquidity sweep
- order-block proximity
- HTF bias
- latest bullish/bearish FVG lifecycle
- iFVG inversion events
- Structure vote
- SMC vote

It returns coordinates/state only. No drawing objects.

### PB_Geometry
Owns coordinate derivation for:
- wedge rails
- wedge apex
- wedge compression
- wedge measured target
- pitchfork median/channel/handles
- pitchfork telemetry
- Kihon/Taito time offsets
- position stop/entry/target levels
- structure-phase label

... (truncated for brevity)