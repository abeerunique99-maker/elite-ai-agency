import sqlite3
from datetime import datetime

DB_FILE = "agency_memory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            model TEXT,
            prompt TEXT,
            response TEXT,
            cost REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(model: str, prompt: str, response: str, cost: float):
    init_db()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO interactions (timestamp, model, prompt, response, cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.utcnow().isoformat(), model, prompt, response, cost))
    conn.commit()
    conn.close()