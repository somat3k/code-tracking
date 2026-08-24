from pathlib import Path
import hashlib
HERE=Path(__file__).resolve().parent
MODULES=HERE/"modules"
ORDER=['00_HEADER_PANEL.pine.part', '01_FOUNDATION_POOL.pine.part', '02_ENGINES_ARTIFACT_POOL.pine.part', '03_EXECUTION_POSITION_SERVICE.pine.part', '04A_RENDER_REGISTRY.pine.part', '04B_FVG_TRANSPORT.pine.part', '04C_REMOTE_PRIMITIVES.pine.part', '05A_WEDGE_CEMENT_FIB.pine.part', '05B_FORK_WAVE_TIME.pine.part', '05C_SIGNAL_WAVE_RECOVERY.pine.part', '05D_FIELD_ORBIT_ANGLE.pine.part', '06_POSITION_WAVE_TIME.pine.part', '07_EDGE_BOARD_SESSION2.pine.part']
OUT=HERE/"PITBULL_Master_Stage7_4_EdgeBoard_Session2.pine"
text="".join((MODULES/name).read_text() for name in ORDER)
OUT.write_text(text)
print(OUT)
print("sha256",hashlib.sha256(text.encode()).hexdigest())
print("lines",len(text.splitlines()))