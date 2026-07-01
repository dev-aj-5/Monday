from services.database import get_connection


VALID_SETTINGS = {
    "prefix",
    "personality",
    "log_channel",
    "welcome_channel",
    "automod",
    "language",
    "timezone"
}


def initialize():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guild_settings (

            guild_id INTEGER PRIMARY KEY,

            prefix TEXT DEFAULT '!',

            personality TEXT DEFAULT 'Monday',

            log_channel INTEGER,

            welcome_channel INTEGER,

            automod INTEGER DEFAULT 0,

            language TEXT DEFAULT 'en',

            timezone TEXT DEFAULT 'UTC'
        )
    """)

    conn.commit()
    conn.close()


def create_guild(guild_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO guild_settings (guild_id)
        VALUES (?)
        """,
        (guild_id,)
    )

    conn.commit()
    conn.close()


def get_setting(guild_id, key):

    if key not in VALID_SETTINGS:
        raise ValueError(f"Invalid setting: {key}")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        f"SELECT {key} FROM guild_settings WHERE guild_id=?",
        (guild_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        create_guild(guild_id)
        return get_setting(guild_id, key)

    return row[key]


def set_setting(guild_id, key, value):

    if key not in VALID_SETTINGS:
        raise ValueError(f"Invalid setting: {key}")

    create_guild(guild_id)

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        f"""
        UPDATE guild_settings
        SET {key}=?
        WHERE guild_id=?
        """,
        (
            value,
            guild_id
        )
    )

    conn.commit()
    conn.close()


def delete_guild(guild_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM guild_settings
        WHERE guild_id=?
        """,
        (guild_id,)
    )

    conn.commit()
    conn.close()