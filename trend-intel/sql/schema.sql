CREATE TABLE IF NOT EXISTS signals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_name TEXT NOT NULL,
  source_type TEXT NOT NULL,
  url TEXT,
  title TEXT,
  snippet TEXT,
  content_text TEXT,
  author TEXT,
  observed_at TEXT NOT NULL,
  published_at TEXT,
  language TEXT,
  geo TEXT,
  engagement_json TEXT,
  raw_payload_json TEXT,
  hash TEXT UNIQUE,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS entities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  signal_id INTEGER NOT NULL,
  entity_text TEXT NOT NULL,
  entity_type TEXT,
  normalized_text TEXT NOT NULL,
  keywords_json TEXT,
  category TEXT,
  confidence REAL,
  FOREIGN KEY(signal_id) REFERENCES signals(id)
);

CREATE TABLE IF NOT EXISTS clusters (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  canonical_name TEXT NOT NULL UNIQUE,
  cluster_type TEXT,
  description TEXT,
  first_seen_at TEXT,
  last_seen_at TEXT,
  status TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS cluster_members (
  cluster_id INTEGER NOT NULL,
  entity_id INTEGER NOT NULL,
  match_score REAL,
  PRIMARY KEY(cluster_id, entity_id),
  FOREIGN KEY(cluster_id) REFERENCES clusters(id),
  FOREIGN KEY(entity_id) REFERENCES entities(id)
);

CREATE TABLE IF NOT EXISTS cluster_metrics_daily (
  cluster_id INTEGER NOT NULL,
  date TEXT NOT NULL,
  signal_count INTEGER DEFAULT 0,
  source_diversity REAL DEFAULT 0,
  engagement_score REAL DEFAULT 0,
  velocity_score REAL DEFAULT 0,
  novelty_score REAL DEFAULT 0,
  commercial_score REAL DEFAULT 0,
  forecast_score REAL DEFAULT 0,
  trend_score REAL DEFAULT 0,
  confidence_score REAL DEFAULT 0,
  PRIMARY KEY(cluster_id, date),
  FOREIGN KEY(cluster_id) REFERENCES clusters(id)
);

CREATE TABLE IF NOT EXISTS reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  report_type TEXT NOT NULL,
  generated_at TEXT NOT NULL,
  payload_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS alerts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cluster_id INTEGER NOT NULL,
  alert_type TEXT NOT NULL,
  triggered_at TEXT NOT NULL,
  reason TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  FOREIGN KEY(cluster_id) REFERENCES clusters(id)
);
