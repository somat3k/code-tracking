# PITBULL Stage 6 • Lossless Feature Ledger

| Capability | Stage 6 owner | Voting role | Status |
|---|---|---:|---|
| FVG lifecycle | PB_Structure | FVG plane | Preserved |
| iFVG inversion | PB_Structure | FVG plane | Preserved |
| BOS / CHoCH | PB_Structure | Structure plane | Preserved |
| Liquidity sweep | PB_Structure | SMC/Liquidity plane | Preserved |
| Order-block proximity | PB_Structure | SMC/Liquidity plane | Preserved |
| Z-score mean reversion | Master CoreState | MR plane | Preserved, Performer removed |
| SuperBoll | Master CoreState | SuperBoll plane | Preserved, shared ATR basis |
| MA / VIDYA / VWAP / crosses | PB_Context v4 | Trend plane | Preserved |
| MTF trend + momentum | Main MTF bridge + PB_Context v4 | MTF plane | Preserved |
| MACD / RSI / cycle / phase | PB_Context v4 | Momentum plane | Preserved |
| Ichimoku | PB_Context v4 | Ichimoku plane | Preserved |
| Convolution / LinReg correction | PB_Context v4 | Correction plane | Preserved |
| Consumed / burned / demand | PB_Context v4 | Orderflow plane | Preserved |
| Wave impulse/corrective/triangle/fibo | PB_Waves v7 | Wave plane | Preserved |
| Wave BODY / SPACE / TIME / FIELD | PB_Waves v7 | Wave plane | Preserved |
| Keltner / Donchian | PB_Waves v7 | Wave local mechanics | Preserved |
| Kihon / Taito time theory | PB_Waves v7 + visuals | Wave local mechanics | Preserved |
| Macro / local range map | Master | Macro/Range plane | Preserved, removed from Governor direction |
| ATR pressure / agreement / conflict | PB_Governor v5 | Permission only | Preserved |
| Risk / FREEZE / INVESTIGATE / RUN+ | PB_Governor v5 | Downstream Governor | Preserved |
| Position sizing / notional cap | Master execution | Execution | Preserved |
| TP / SL / frozen entry ATR mechanics | Master execution | Execution | Preserved |
| Wedge | PB_Geometry | Non-voting service | Preserved |
| Pitchfork | PB_Geometry | Non-voting service | Preserved |
| Projection Cement | PB_Geometry | Non-voting service | Preserved |
| Dimensional Field | PB_Geometry | Non-voting service | Preserved |
| FVG boxes / iFVG history | Master renderer | Presentation | Preserved |
| Wave board / wave ledger | Master renderer | Presentation | Preserved |
| Fibonacci ladder | Master renderer | Presentation | Preserved |
| Cycle orbit / time rails | Master renderer | Presentation | Preserved |
| Position corridor / ledger / trace | Master renderer | Presentation | Preserved |
| Plot-Save registry | Master registry | Presentation | Preserved |
| Command / protocol decks | Master tables | Presentation | Preserved |

## Deliberately deleted infrastructure

These are not market features and are intentionally gone:

- `PB_Performer` composite score routing
- `PB_Router`
- PITBULL / MULTIPLEXER / WEIGHTED modes
- MUX Trend / Range / Volatile / Transition matrices
- Router event / weighted mix matrices
- Context consensus weight panel
- Reliability min/max weighting panel
- repeated ATR length controls
... (truncated for brevity)