# Stage 8 profile matrix

Both profiles preserve the same plane contracts, score semantics, visual form,
and TradingView's 64-plot ceiling. Neither generated profile exists yet.

| Contract | Core | Premium |
|---|---|---|
| Plot budget | 52 soft, 64 hard | 52 soft, 64 hard |
| Configured request target | 12 | 12 |
| Board surfaces | 3 | 3 |
| Plan-limited data dependencies | Excluded | Allowed only behind an explicit profile adapter |
| Fallback behavior | Required | Required when premium data is unavailable |
| Verification | Static plus TradingView/replay | Static plus TradingView/replay on an entitled account |

Profile selection must happen at build time. A runtime toggle must not leave a
Core build dependent on plan-limited requests or imported library scopes.