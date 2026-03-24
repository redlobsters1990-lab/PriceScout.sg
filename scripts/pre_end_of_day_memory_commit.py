#!/usr/bin/env python3
from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path

ROOT = Path('/Users/chozengone/.openclaw/workspace-main')
MEMORY = ROOT / 'memory'
TODAY = datetime.now().strftime('%Y-%m-%d')
DEFAULT_RUN_ID = f'{TODAY}-run-001'
RUN_DIR = MEMORY / 'runs' / DEFAULT_RUN_ID
DAILY_STATE = MEMORY / 'daily_state' / f'{TODAY}.md'
ARCHIVE_DIR = MEMORY / 'archive' / TODAY
KNOWLEDGE_DIR = MEMORY / 'knowledge'
LOG_PATH = RUN_DIR / 'memory_commit_log.md'
SUMMARY_JSON = RUN_DIR / 'memory_commit_summary.json'

PROMOTION_TARGETS = {
    'validated_opportunities': KNOWLEDGE_DIR / 'validated_opportunities.md',
    'reusable_rejection_reasons': KNOWLEDGE_DIR / 'rejected_patterns.md',
    'serp_patterns': KNOWLEDGE_DIR / 'serp_patterns.md',
    'confirmed_monetization_sources': KNOWLEDGE_DIR / 'monetization_sources.md',
    'dataset_structures': KNOWLEDGE_DIR / 'dataset_models.md',
    'proven_page_blueprints': KNOWLEDGE_DIR / 'page_blueprint_patterns.md',
}


def ensure_dirs() -> None:
    for path in [RUN_DIR, ARCHIVE_DIR, KNOWLEDGE_DIR, MEMORY / 'daily_state']:
        path.mkdir(parents=True, exist_ok=True)


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def append_section(path: Path, heading: str, bullet_lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text() if path.exists() else f'# {path.stem.replace("_", " ").title()}\n\n'
    body = '\n'.join(f'- {line}' for line in bullet_lines if line)
    if not body:
        return
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    existing += f'\n## {heading} ({stamp})\n{body}\n'
    path.write_text(existing)


def update_daily_state(summary: dict) -> None:
    if DAILY_STATE.exists():
        text = DAILY_STATE.read_text().rstrip() + '\n\n'
    else:
        text = f'# Daily State — {TODAY}\n\n'
    text += '## End-of-day memory commit\n'
    sections = [
        ('Opportunities discovered', summary.get('opportunities_discovered', [])),
        ('Opportunities rejected', summary.get('opportunities_rejected', [])),
        ('Opportunities approved', summary.get('opportunities_approved', [])),
        ('Patterns learned', summary.get('patterns_learned', [])),
        ('Unresolved tasks', summary.get('unresolved_tasks', [])),
        ('Carryover items', summary.get('carryover_items', [])),
    ]
    for heading, items in sections:
        text += f'\n### {heading}\n'
        if items:
            text += '\n'.join(f'- {item}' for item in items) + '\n'
        else:
            text += '- none\n'
    DAILY_STATE.write_text(text)


def promote(summary: dict) -> list[str]:
    promoted = []
    for key, target in PROMOTION_TARGETS.items():
        items = summary.get(key, [])
        if items:
            append_section(target, f'Promoted from {DEFAULT_RUN_ID}', items)
            promoted.extend([f'{key}: {item}' for item in items])
    return promoted


def move_evidence() -> list[str]:
    moved = []
    evidence_dir = RUN_DIR / 'evidence'
    if not evidence_dir.exists():
        return moved
    for item in evidence_dir.iterdir():
        target = ARCHIVE_DIR / item.name
        item.rename(target)
        moved.append(f'{item.name} -> {target.relative_to(ROOT)}')
    return moved


def write_log(summary: dict, promoted: list[str], archived: list[str]) -> None:
    lines = [
        f'# Memory Commit Log — {DEFAULT_RUN_ID}',
        '',
        f'- Date: {TODAY}',
        f'- Run ID: {DEFAULT_RUN_ID}',
        '',
        '## Promoted to knowledge',
    ]
    lines += [f'- {item}' for item in promoted] or ['- none']
    lines += ['', '## Archived evidence']
    lines += [f'- {item}' for item in archived] or ['- none']
    lines += ['', '## Kept in run memory']
    kept = summary.get('kept_in_run_memory', [])
    lines += [f'- {item}' for item in kept] or ['- current run outputs remain in place']
    lines += ['', '## Not stored']
    skipped = summary.get('not_stored', [])
    lines += [f'- {item}' for item in skipped] or ['- none']
    LOG_PATH.write_text('\n'.join(lines) + '\n')


def main() -> None:
    ensure_dirs()
    summary = load_json(SUMMARY_JSON, {
        'opportunities_discovered': [],
        'opportunities_rejected': [],
        'opportunities_approved': [],
        'patterns_learned': [],
        'unresolved_tasks': [],
        'carryover_items': [],
        'validated_opportunities': [],
        'reusable_rejection_reasons': [],
        'serp_patterns': [],
        'confirmed_monetization_sources': [],
        'dataset_structures': [],
        'proven_page_blueprints': [],
        'kept_in_run_memory': [],
        'not_stored': [],
    })
    promoted = promote(summary)
    update_daily_state(summary)
    archived = move_evidence()
    write_log(summary, promoted, archived)
    print(json.dumps({
        'daily_state': str(DAILY_STATE.relative_to(ROOT)),
        'log': str(LOG_PATH.relative_to(ROOT)),
        'promoted_count': len(promoted),
        'archived_count': len(archived),
    }, indent=2))


if __name__ == '__main__':
    main()
