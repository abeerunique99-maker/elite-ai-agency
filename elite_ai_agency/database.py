
import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "agency_metrics.db")

def init_db():
    """
    تهيئة قاعدة بيانات SQLite لتخزين سجلات الاستخدام وتتبع التكاليف.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usage_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            model_used TEXT,
            prompt_length INTEGER,
            cost_status TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_request(model_used: str, prompt_length: int, cost_status: str):
    """
    تسجيل كل عملية توليد يتم تنفيذها لمراقبة الاستهلاك والميزانية.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usage_logs (model_used, prompt_length, cost_status)
        VALUES (?, ?, ?)
    """, (model_used, prompt_length, cost_status))
    conn.commit()
    conn.close()
