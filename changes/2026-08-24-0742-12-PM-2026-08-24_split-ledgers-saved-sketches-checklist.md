# Split-ledger and saved-sketch TradingView checklist

Status: pending authenticated TradingView execution.

Record the TradingView build number, symbol, timeframe, market state, input
preset, timestamp, and screenshot filename for every run.

## Compile and resource gate

- [ ] Pine v6 compiler reports zero errors and zero warnings requiring action.
- [ ] Compiled plot count remains below 64.
- [ ] No request, drawing, table, or execution-limit runtime error appears.
- [ ] Strategy order markers and backtest order count match the pre-session
      reference on the same symbol, timeframe, range, and properties.

## Table placement

- [ ] `top_left` collective data begins below one empty title-height row.
- [ ] `top_right` Position data begins below one empty title-height row.
- [ ] `middle_right` Wave data begins below one empty title-height row.
- [ ] Symbol/logo/OHLCV/indicator status text does not cover a readable cell at
      default scale and after horizontal/vertical chart resize.
- [ ] Position ledger shows state/R, quantity/exposure, entry/current,
      stop/target, RR/MFE/MAE, held time, and last exit.
- [ ] Wave ledger shows identity/state/status, completion/target,
      cumulative/volume/amount, time fit, body/space, and episode probabilities.
- [ ] Disabling each ledger clears only that ledger; collective cards remain.

## Saved-sketch lifecycle

- [ ] With the market open, reload the chart: wedge, Swing/Cement Fib,
      dimensional rectangle/triangle, circle/orbit, spiral, and vector rebuild
      from the last confirmed historical state without waiting for bar close.
- [ ] During at least 20 realtime ticks, retained sketches do not disappear,
      clear/recreate, or jump to unconfirmed geometry.
- [ ] A transient invalid Cement/Field/Wedge calculation holds the last valid
      sketch.
- [ ] The next confirmed valid measurement updates the existing family once.
- [ ] An explicit family toggle off clears that family; toggling it on rebuilds
      on a confirmed snapshot.
- [ ] Bar Replay across pivot changes replaces Swing Fib rails without a blank
      intermediate frame.
- [ ] Plot-Save diagnostics remain within effective registry budgets and no
      protected sketch family is evicted by global pruning.

## Evidence files

- Compile note:
- Reload screenshot:
- Tick-stability capture:
... (truncated for brevity)