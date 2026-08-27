# Superseded hyper-aggressive profile

This preserved design note is not the active default. The active Stage 8 master now uses the zero-genesis score configuration: all strategy toggles are off, all score/mixture weights are zero, and score gates are unconfigured until the user explicitly sets them.

This profile accelerates signal discovery while retaining the existing closed-bar execution, governor, frozen-entry ATR, notional cap, and stop/target services.

## Fast trigger layer

- ATR: 14
- normalization clamp: 2.05
- pivots: 3 / 3
- Keltner: EMA 10 with 1.25 ATR
- mean reversion: Z 14, thresholds -1.8 / +1.8, pullback window 8
- SuperBoll: 55
- base long/short threshold: +/-0.54

## Slow regime layer

- ATR baseline: 200
- trend smoothing: 14 / 200 / 254
- DMI/ADX: 201 / 201
- ADX membership: zero at 12, full at 35
- regime confirmation: 2 bars

ADX is conviction-only. Direction comes from DMI and the 200/254 EMA spread. During warm-up, the performance membership degrades to neutral rather than blocking trades.

## Pool priors

| Plane | Weight |
| --- | ---: |
| FVG | 1.35 |
| Structure | 1.25 |
| SMC | 0.85 |
| Mean reversion | 1.10 |
| SuperBoll | 1.05 |
| Trend | 1.10 |
| MTF | 0.75 |
| Momentum | 1.30 |
| Ichimoku | 0.80 |
| Correction | 0.90 |
| Order flow | 1.15 |
| Wave | 1.20 |
| Macro/range | 0.70 |

The existing pool independence discount remains active. The slow regime may alter fast-plane effective weights only within 0.86 to 1.14. In aligned high-ADX conditions, the actual decision gate can contract by at most 0.04; opposition raises it by at most 0.02. The absolute decision-gate floor is 0.48.

## TradingView release gate

Local static checks prove source consistency and resource-policy compliance, not profitability or TradingView runtime behavior. Before live use, compile the generated master in TradingView, check the first 300 bars for ADX warm-up behavior, compare trade count and drawdown against the Stage 7.4 baseline, and validate on out-of-sample symbols and timeframes with commission and slippage appropriate to the venue.