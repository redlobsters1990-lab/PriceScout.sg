import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from .db import connect, init_db
from .settings import DATA_DIR, REPORTS_DIR


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def cmd_init(_: argparse.Namespace) -> None:
    init_db()
    print("initialized")


def cmd_collect(_: argparse.Namespace) -> None:
    init_db()
    sample = {
        "collected_at": now_iso(),
        "status": "stub",
        "message": "collector scaffold ready; connect RSS/web/reddit/github collectors next"
    }
    out = DATA_DIR / "raw" / f"collect-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    out.write_text(json.dumps(sample, indent=2))
    print(out)


def cmd_normalize(_: argparse.Namespace) -> None:
    init_db()
    sample = {
        "normalized_at": now_iso(),
        "status": "stub",
        "message": "normalization scaffold ready"
    }
    out = DATA_DIR / "normalized" / f"normalize-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    out.write_text(json.dumps(sample, indent=2))
    print(out)


def cmd_cluster(_: argparse.Namespace) -> None:
    init_db()
    print("cluster scaffold ready")


def cmd_score(_: argparse.Namespace) -> None:
    init_db()
    print("score scaffold ready")


def cmd_report(_: argparse.Namespace) -> None:
    init_db()
    report = {
        "generated_at": now_iso(),
        "current_trends": [],
        "emerging_trends": [],
        "watchlist": [],
        "notes": [
            "report scaffold ready",
            "wire collectors and scoring before trusting this output"
        ]
    }
    out = REPORTS_DIR / f"daily-{datetime.now().strftime('%Y%m%d')}.json"
    out.write_text(json.dumps(report, indent=2))
    with connect() as conn:
        conn.execute(
            "INSERT INTO reports(report_type, generated_at, payload_json) VALUES (?, ?, ?)",
            ("daily", now_iso(), json.dumps(report)),
        )
        conn.commit()
    print(out)


def cmd_alert(_: argparse.Namespace) -> None:
    init_db()
    print("alert scaffold ready")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="trend-intel")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, fn in {
        "init-db": cmd_init,
        "collect": cmd_collect,
        "normalize": cmd_normalize,
        "cluster": cmd_cluster,
        "score": cmd_score,
        "report-daily": cmd_report,
        "alert": cmd_alert,
    }.items():
        p = sub.add_parser(name)
        p.set_defaults(func=fn)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
