# Stage 5.0 • Publication order

The six upgraded libraries do not depend on each other. They depend only on
already-stable PB_Types / PB_Math / PB_Structure where applicable.

Suggested publication sequence:

1. PB_Performer_v3.pine      -> expected import PB_Performer/3
2. PB_Context_v3.pine        -> expected import PB_Context/3
3. PB_Waves_v6.pine          -> expected import PB_Waves/6
4. PB_Governor_v3.pine       -> expected import PB_Governor/3
5. PB_Router_v3.pine         -> expected import PB_Router/3
6. PB_Geometry_v5.pine       -> expected import PB_Geometry/5
7. PITBULL_Master_Stage5_0_ParameterSovereignty.pine

TradingView publication numbers are authoritative.

If TradingView assigns a different version to any library, change only the
corresponding import line in the master. Do not republish an older API under
the new version number.