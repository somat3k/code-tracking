# Source of truth

## Frozen release

`versions/v7.4.0-baseline/full-project/` is a complete byte-preserving snapshot of the former `project strindy` tree.

The snapshot intentionally retains three `.DS_Store` files because they were present in the source tree and are covered by `MANIFEST.sha256`. They are the only workstation metadata files eligible for version control; `.gitignore` excludes all others.

`versions/v7.4.0-baseline/canonical/` extracts the Stage 7.4 Session 3 master and the direct/transitive Pine sources needed to understand its pinned imports.

The authoritative Stage 7.4 master is:

`canonical/master/PITBULL_Master_Stage7_4_EdgeBoard_Final_Session3.pine`

## Canonical dependency map

| Published import | Local source retained |
|---|---|
| `PB_Types/1` | `PB_Types_v1.pine` |
| `PB_Math/2` | `PB_Math_v2.pine` |
| `PB_Structure/1` | `PB_Structure_v1.pine` |
| `PB_Governor/5` | `PB_Governor_v5.pine` |
| `PB_Context/4` | `PB_Context_v4.pine` |
| `PB_Waves/7` | `PB_Waves_v7.pine` |
| `PB_Geometry/6` | `PB_Geometry_v6.pine` |
| `PB_SliceTransport/1` | `PB_SliceTransport_v1.pine` |
| `PB_ArtifactCore/1` | `PB_ArtifactCore_v1.pine` |

The master directly imports eight libraries. `PB_Math/2` is the one additional transitive dependency, producing nine unique canonical library sources.

An alternate loose `PB_Structure_v1` copy had drifted to an import of `PB_Math/1`. It is preserved under `reference/legacy-library-alternates/`, but it is not canonical. The retained canonical Structure source matches the archived Stage 4 package and imports `PB_Math/2`. The locally retained Math `/1` alternate is byte-identical to `/2`, but the published identity must remain `/2`.

## Known provenance issue

The retained Session 2 shard package rebuilds the Session 2 master, not the manually finalized Session 3 master. It is stored under `reference/` for source mapping only. Stage 8 now has 13 canonical Session 3 shards under `upgrades/v8.0.0-development/src/modules/`; `BASELINE_MODULE_MANIFEST.json` records the byte-exact reconstruction contract.

`PB_Geometry/6` is preserved because that is what the Stage 7.4 master imports. `PB_Geometry_v7` is retained only as an upgrade candidate under the Stage 8 references and must not silently replace the pinned version.

## Working source

Only files under `upgrades/v8.0.0-development/src/` are intended to change during the next implementation. When Stage 8 is released, its exact generated package will be copied into a new immutable folder under `versions/`.