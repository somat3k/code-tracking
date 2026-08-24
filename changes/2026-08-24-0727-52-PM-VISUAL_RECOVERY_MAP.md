# PITBULL Stage 3 v2 • Visual Contract Recovery

The supplied PITBULL v14 monolith is treated as the reference surface for this
recovery. Stage 3 libraries remain analytical; the Master Orchestrator owns
TradingView drawing objects.

## Ownership

### PB_Context v2
Returns:
- candle body/range, upper/lower wick and close-location telemetry
- volume consumed, volume burned and demand availability
- MACD / RSI / VWAP / MA / VIDYA / cycle state
- MTF trend and momentum
- Ichimoku Tenkan / Kijun / Span A / Span B
- cloud top / bottom / midpoint / thickness in ATR / price-to-cloud distance
- Tenkan-cross, Kijun-cross and Kumo-twist events
- correction tunnel / regression state
- trend / momentum / volatility votes
- regime persistence
- score-target / Ichimoku confluence helper

Creates:
- no lines
- no boxes
- no labels
- no tables

### PB_Waves v2
Returns:
- impulse / corrective / triangle probabilities
- Fibonacci confluence
- recovery / momentum / composite
- live wave origin, direction, amount, ATR amount, %, progress, target
- cumulative volume and normalized volume X
- elapsed bars / minutes
- one-bar newEpisode event
- episode number, prior/current pivots, path direction and leg
- episode probability / cumulative confidence / target / name / goal

Creates:
- no lines
- no boxes
- no labels
- no tables

### Master Orchestrator Stage 4.2
Owns the visible chart surface.

Recovered visual families:
... (truncated for brevity)