from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "db"
CONFIG_DIR = ROOT / "config"
REPORTS_DIR = DATA_DIR / "reports"
DB_PATH = DB_DIR / "trendintel.sqlite"
SCHEMA_PATH = ROOT / "sql" / "schema.sql"

for path in [DATA_DIR, DB_DIR, REPORTS_DIR, DATA_DIR / "raw", DATA_DIR / "normalized"]:
    path.mkdir(parents=True, exist_ok=True)
