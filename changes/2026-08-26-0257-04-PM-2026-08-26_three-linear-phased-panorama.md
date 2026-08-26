# Three-linear phased Panorama

## Request identity

- Date: 2026-08-26
- Requested by: PITBULL owner
- Target upgrade/version: `v8.0.0-development`
- Short name: `three-linear-phased-panorama`
- Priority: High

## Desired outcome

PITBULL presents one persistent price-anchored Panorama divided into three
directional fields. The upper field is bullish, the middle field is a neutral
phase/time core, and the lower field is bearish. Each field exposes the maximum
causal data already available from the libraries through bounded linework,
measurements, fractions, channels, clouds, volume evidence, breakout and
pullback state.

The display must answer four questions without changing execution ownership:

1. Which directional field is active?
2. How much confirmed price/time space remains in either direction?
3. Which length, phase and evidence family supports each route?
4. Where are continuation, pullback and invalidation coordinates?

## Scope

- Strategy planes affected: read-only consumption of all completed plane scores.
- Data/MTF affected: confirmed OHLCV, confirmed MTF context and missing-volume state.
- Execution/risk affected: none in the first renderer release; later quantity deltas must route through Governor.
- Renderer families affected: new bounded `PANORAMA` line, box and label family.
- Board/cards affected: existing top/left/bottom Edge Board frame gains Panorama summaries.
- Libraries affected: `PB_ArtifactCore`, `PB_Waves`, `PB_Geometry`, `PB_Structure`, `PB_SliceTransport`; existing APIs remain compatible within publication version constraints.

## Preserve exactly

- Existing Stage 7.4 structure/form to preserve: three-table Edge Board frame and all existing instruments.
- Visual elements that must remain: Position, Wave, FVG, Geometry, Field, Ichimoku, score and event cards.
- Strategy behavior that must not change: order calls, order ownership, sizing, SL/TP and closed-bar entry policy.
- Inputs/import versions that must not change: published library import versions until upgraded libraries compile in publication order.

## Requested change

### Upper bullish field

- Confirmed bullish BOS/CHoCH, breakout acceptance and pullback/retest state.
- Bullish FVG, demand, volume pressure and HA evidence.
- Upper Donchian/Keltner/cloud/pivot destinations.
- Adaptive ATR/Fibonacci divisions and expected time windows.
... (truncated for brevity)