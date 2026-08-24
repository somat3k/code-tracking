# Heikin-Ashi Volume kernel TradingView checklist

Status: pending authenticated TradingView execution.

Record the TradingView build number, symbol, timeframe, chart type, market
state, input preset, timestamp, strategy export, and screenshot filename.

## Compile and isolation

- [ ] Pine v6 compiler reports zero errors and zero warnings requiring action.
- [ ] Compiled plot count remains unchanged and below 64.
- [ ] The configured request-context count remains unchanged.
- [ ] HA Volume ON and OFF produce identical strategy orders, fills, P/L, and
      order count on the same symbol, timeframe, range, and properties.
- [ ] No drawing-limit, future-coordinate, or execution-time runtime error occurs.

## Candle geometry

- [ ] Test on a standard candlestick chart; HA bodies follow synthetic HA OHLC
      while strategy fills remain on real market prices.
- [ ] Bull, bear, and doji colors match their HA open/close relationship.
- [ ] Full low-to-high wicks remain visible above and below each body.
- [ ] RVOL tiers visibly progress through tight, small, normal, and fat bodies.
- [ ] Maximum-width bodies remain centered on their source candle and do not
      cover multiple neighboring bar slots at the default 82% setting.
- [ ] The newest callout has three square segments, one deliberate break, and a
      readable phase/RVOL/width/wick/HA-OHLC label above the leader.

## Lifecycle and pressure

- [ ] At history 24, diagnostics never exceed 24 HA bodies, 24 HA wicks, three
      callout lines, and one callout label.
- [ ] Twenty realtime ticks do not move or blink the last confirmed packet.
- [ ] Reload during an open market restores the last 24 confirmed candles and
      one latest callout without waiting for the realtime bar to close.
- [ ] Bar Replay advances one candle packet per confirmed bar without duplicates.
- [ ] Disabling only the callout clears its three lines and label but retains
      candle history.
- [ ] Disabling HA Volume or Plot-Save clears all HA families and leaves the
      collective board and operational geometry intact.
- [ ] Under maximum drawing pressure, older HA history sheds before protected
      wedge, Fibonacci, Field, Position, and Cement families.

## Missing volume

- [ ] On a symbol with no usable volume, candles still render with neutral width.
- [ ] The callout explicitly displays `VOLUME N/A`; no divide-by-zero or `na`
      coordinate error occurs.

## Evidence files
... (truncated for brevity)