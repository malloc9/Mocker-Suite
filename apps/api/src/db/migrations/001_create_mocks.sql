CREATE TABLE IF NOT EXISTS mocks (
  id TEXT PRIMARY KEY,            -- UUID for each mock
  method TEXT NOT NULL,           -- 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'
  path TEXT NOT NULL,            -- e.g., '/api/users'
  response_status INTEGER NOT NULL DEFAULT 200, -- HTTP status code
  response_body TEXT,            -- JSON string for the response body
  response_headers TEXT,         -- JSON string for key-value header pairs
  description TEXT,              -- A user-friendly name or description
  is_active INTEGER NOT NULL DEFAULT 1, -- 0 or 1 to quickly toggle the mock
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE UNIQUE INDEX idx_method_path ON mocks (method, path);