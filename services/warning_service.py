import sqlite3
from services.database import get_connection


def initialize():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warnings (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            guild_id INTEGER,

            user_id INTEGER,

            moderator_id INTEGER,

            reason TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def warn(guild_id, user_id, moderator_id, reason):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warnings
        (guild_id, user_id, moderator_id, reason)
        VALUES (?, ?, ?, ?)
        """,
        (
            guild_id,
            user_id,
            moderator_id,
            reason
        )
    )

    conn.commit()
    conn.close()


def get_warnings(guild_id, user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT reason, created_at
        FROM warnings
        WHERE guild_id=? AND user_id=?
        ORDER BY created_at DESC
        """,
        (
            guild_id,
            user_id
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def clear_warnings(guild_id, user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM warnings
        WHERE guild_id=? AND user_id=?
        """,
        (
            guild_id,
            user_id
        )
    )

    conn.commit()
    conn.close()