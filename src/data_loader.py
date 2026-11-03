from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def load_data(raw_dir: Path = RAW_DIR):
    """Load the two raw NHANES XPT files."""
    demo = pd.read_sas(raw_dir / "DEMO_L.xpt")
    bmx = pd.read_sas(raw_dir / "BMX_L.xpt")
    return demo, bmx


def merge_data(demo: pd.DataFrame, bmx: pd.DataFrame) -> pd.DataFrame:
    """Merge demographic and body-measure data using SEQN."""
    if not demo["SEQN"].is_unique or not bmx["SEQN"].is_unique:
        raise ValueError("SEQN must be unique in both input files.")
    return demo.merge(bmx, on="SEQN", how="inner")
