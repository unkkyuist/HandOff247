"""SQLite access. Every statement the application runs is in this file."""
import os
import sqlite3

DB_PATH = os.environ.get("NEWSROOM_DB", "newsroom.db")


def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def query(sql, params=()):
    with connect() as con:
        return con.execute(sql, params).fetchall()


def execute(sql, params=()):
    with connect() as con:
        con.execute(sql, params)


def get_user(user_id):
    rows = query("SELECT id, email, role FROM users WHERE id = ?", (user_id,))
    return rows[0] if rows else None


def find_user(email):
    rows = query("SELECT id, email, role FROM users WHERE email = ?", (email,))
    return rows[0] if rows else None


def get_article(article_id):
    rows = query("SELECT * FROM articles WHERE id = ?", (article_id,))
    return rows[0] if rows else None


def articles_of(author_id):
    return query("SELECT id, title, status, review_note FROM articles WHERE author_id = ? ORDER BY id DESC", (author_id,))


def create_article(author_id, title, body, cover):
    execute("INSERT INTO articles (author_id, title, body, cover, status) VALUES (?, ?, ?, ?, 'draft')",
            (author_id, title, body, cover))


def send_for_review(article_id):
    execute("UPDATE articles SET status = 'in_review' WHERE id = ?", (article_id,))


def waiting_for_review():
    return query("SELECT id, title, cover FROM articles WHERE status = 'in_review' ORDER BY id")


def publish_article(article_id):
    execute("UPDATE articles SET status = ?, published_at = CURRENT_TIMESTAMP WHERE id = ?", ("published", article_id))


def return_to_author(article_id, reason):
    execute("UPDATE articles SET status = 'draft', review_note = ? WHERE id = ?", (reason, article_id))


def published_articles():
    return query("SELECT id, title, cover FROM articles WHERE status = 'published' ORDER BY published_at DESC")
