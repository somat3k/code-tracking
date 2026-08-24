# PITBULL Stage 6.4 • Drawing Federation Ledger

Stage 6.4 makes drawing ownership independent in the same spirit as the score-plane federation.

| Family | Owner / trigger | Lifecycle | Performance rule |
|---|---|---|---|
| Pivot anchors | Structure pivots | historical bounded | create once per new pivot |
| FVG core | Structure latest FVG | current | closed-bar setter reuse |
| FVG history | Drawing federation | fresh → partial → filled → expiry | max 8 |
| iFVG | Structure inversion event | historical bounded | existing event history |
| Order Blocks | SMC plane + engulfing body search | active until invalidation | max 8 |
| Wedge | PB_Geometry Wedge | forming / compressing / ready / breakout | rails update only when pivot geometry changes |
| Projection Cement | PB_Geometry Cement | current confluence geometry | existing Plot-Save reuse |
| Fibonacci Swing | latest high/low pivots | one active swing frame | rebuild only when pivot pair changes |
| Pitchfork | PB_Geometry Fork | current structural fork | rays update only when A/B/C changes |
| Fork levels | PB_Geometry Fork | current | three short closed-bar dashes |
| Wave path | PB_Waves | current / event | existing persistent path |
| Wave cards | material wave change | historical bounded | recycle oldest handles |
| Ichimoku Time | Context / Wave time | current forecast rails | closed-bar commit |
| Signal geometry | final pool signal | event | bounded history |
| Score range | score thresholds | current | persistent setters |
| Dimensional Field | PB_Geometry Field | current | Plot-Save keyed families |
| Cycle Orbit | latest pivot pair | structural | rebuild only on pivot-pair change |
| Pivot Angle | latest pivot pair | structural | rebuild only on pivot-pair change |
| Position corridor | actual position | active trade | persistent Plot-Save |
| Position trace | actual position | historical active trace | modulo handle ring |
| Position exits | actual exit | historical bounded | existing prune budget |

## Visibility changes

Stage 6.4 intentionally reveals several methodologies that existed but were visually quiet:

- Wave Keltner / Donchian defaults ON.
- FVG halo defaults ON.
- FVG data defaults ON.
- Fibonacci labels default ON.
- Cycle Orbit no longer disappears just because Dimensional Field is enabled.

Projection Cement still calculates Wedge and Fibonacci confluence. Dedicated Wedge and Fibonacci instruments now own those visible rails to prevent duplicated rendering.