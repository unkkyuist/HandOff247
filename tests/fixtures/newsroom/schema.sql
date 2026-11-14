CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  author_id INTEGER NOT NULL REFERENCES users(id),
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  cover TEXT,
  status TEXT NOT NULL DEFAULT 'draft',
  review_note TEXT,
  published_at TEXT
);
