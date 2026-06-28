import sqlite3
from pathlib import Path

# --------------------------------------------------
# Database Location
# --------------------------------------------------

DB_PATH = Path("data") / "memory.db"

DB_PATH.parent.mkdir(exist_ok=True)


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

def initialize():

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    category TEXT NOT NULL,

    memory_key TEXT NOT NULL,

    memory_value TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(user_id, memory_key)
)
""")

    connection.commit()

    connection.close()


# --------------------------------------------------
# Remember
# --------------------------------------------------

def remember(user_id, category, key, value):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO memories

        (user_id, category, memory_key, memory_value)

        VALUES (?, ?, ?, ?)

        ON CONFLICT(user_id, memory_key)

        DO UPDATE SET

            memory_value = excluded.memory_value,

            category = excluded.category,

            updated_at = CURRENT_TIMESTAMP
        """,

        (
            user_id,
            category,
            key,
            value
        )
    )

    connection.commit()

    connection.close()
# --------------------------------------------------
# Recall
# --------------------------------------------------

def recall(user_id, key):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT memory_value

        FROM memories

        WHERE

            user_id = ?

            AND memory_key = ?
        """,

        (
            user_id,
            key
        )
    )

    result = cursor.fetchone()

    connection.close()

    if result:

        return result[0]

    return None

# --------------------------------------------------
# Forget
# --------------------------------------------------

def forget(user_id, key):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM memories

        WHERE

            user_id = ?

            AND memory_key = ?
        """,

        (
            user_id,
            key
        )
    )

    connection.commit()

    connection.close()
# --------------------------------------------------
# List Memories
# --------------------------------------------------

def list_memories(user_id):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            category,

            memory_key,

            memory_value

        FROM memories

        WHERE user_id = ?
        """,

        (
            user_id,
        )
    )

    rows = cursor.fetchall()

    connection.close()

    return rows