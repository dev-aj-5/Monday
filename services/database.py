from pathlib import Path
import sqlite3

DATA_FOLDER = Path("data")
DATA_FOLDER.mkdir(exist_ok=True)

DATABASE_PATH = DATA_FOLDER / "monday.db"


def get_connection():

    conn = sqlite3.connect(DATABASE_PATH)

    conn.row_factory = sqlite3.Row

    return conn