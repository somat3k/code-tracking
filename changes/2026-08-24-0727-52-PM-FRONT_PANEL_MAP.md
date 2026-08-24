# PITBULL Stage 6 • Front Panel

Stage 6 treats the panel as an operator console, not an internal wiring diagram.

## 00 • BASIS • SET ONCE
One ATR length, one ATR baseline, one normalization horizon, one pivot basis and the final long/short score gates.

## 01 • SCORE POOL
Every strategy plane has exactly two global controls:
- Enable
- Weight

Planes:
FVG/iFVG, Structure, SMC/Liquidity, Mean Reversion, SuperBoll, Trend, MTF, Momentum, Ichimoku, Correction, Orderflow, Wave, Macro/Range.

`OFF` removes the plane from both numerator and denominator.

## 02–08 • Local strategy controls
Only high-value local mechanics remain visible:
- FVG/Structure: BOS sensitivity, CHoCH momentum, FVG life.
- MR/SuperBoll: Z length, symmetric Z limits, pullback, SB length.
- Trend/MTF: MA triplet and three timeframes.
- Ichimoku/Correction: one Ichimoku profile plus correction shape.
- Wave: progress, episode target, recovery and momentum.
- Macro/Governor: macro/local range and risk gates.
- Execution: risk %, notional cap, Governor sizing, TP/SL.

## 09–12 • Presentation
Geometry, visuals, recovery and Plot-Save remain available. Low-value micro-tuning such as object alpha, card offsets, segment counts, internal geometry weights and registry budgets is fixed internally.

### Result
The Stage 5.1.1 panel exposed 475 inputs.
Stage 6 exposes 122.
The removed 353 controls are not removed features. They are mostly repeated baselines, local coefficient plumbing, legacy Router infrastructure and presentation micro-tuning.