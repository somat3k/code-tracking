# Stage 8 resource budget

These are project soft caps, not TradingView hard limits.

| Resource | Project cap |
|---|---:|
| Plot counts, Core | 52 |
| Plot counts, Premium | 56 |
| Lines | 440 |
| Boxes | 340 initially; never above declaration limit |
| Labels | 420 |
| Polylines | 40 |
| Unique `request.*()` contexts | 12 target; 40 compatibility ceiling |
| Tables | 3 retained |

## Ownership

- The renderer tracks total live objects, including formerly unmanaged families.
- Candle history is bounded and adapts to remaining capacity.
- Callouts are event-prioritized rather than created on every bar.
- Tables are updated on the last bar and do not consume plot counts.
- Plot-count estimates are advisory until TradingView reports the compiled count.

Any request that changes a resource count must record the expected and measured delta in its completion record.