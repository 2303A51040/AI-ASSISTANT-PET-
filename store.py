import sqlite3
from shared.config import DATABASE_PATH

def connect():
    return sqlite3.connect(DATABASE_PATH)

def init_db():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS conversations (id INTEGER PRIMARY KEY, user_text TEXT NOT NULL, assistant_text TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")
        db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")
        db.execute("CREATE TABLE IF NOT EXISTS meetings (id INTEGER PRIMARY KEY, title TEXT NOT NULL, transcript TEXT NOT NULL, summary TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")

def add_conversation(user_text, assistant_text):
    init_db()
    with connect() as db:
        db.execute("INSERT INTO conversations(user_text, assistant_text) VALUES (?,?)", (user_text, assistant_text))

def add_note(title, body):
    init_db()
    with connect() as db:
        db.execute("INSERT INTO notes(title, body) VALUES (?,?)", (title, body))

def recent_notes(limit=10):
    init_db()
    with connect() as db:
        return db.execute("SELECT title, body, created_at FROM notes ORDER BY id DESC LIMIT ?", (limit,)).fetchall()

def add_meeting(title, transcript, summary):
    init_db()
    with connect() as db:
        db.execute("INSERT INTO meetings(title, transcript, summary) VALUES (?,?,?)", (title, transcript, summary))
