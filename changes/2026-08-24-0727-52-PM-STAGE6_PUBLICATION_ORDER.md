# Stage 6 • Publication order

Publish the changed libraries first:

1. `PB_Context_v4.pine`
2. `PB_Waves_v7.pine`
3. `PB_Governor_v5.pine`

Then compile:

4. `PITBULL_Master_Stage6_FederatedRebuild.pine`

Expected master imports:

- `PB_Types/1`
- `PB_Governor/5`
- `PB_Context/4`
- `PB_Waves/7`
- `PB_Structure/1`
- `PB_Geometry/6`

TradingView publication numbers are authoritative. If TradingView assigns another version, update only the corresponding import suffix.