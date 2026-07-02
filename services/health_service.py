import time
import sqlite3

from services.config_service import get

config = get()

from config import AI_PROVIDER_ORDER

START_TIME = time.time()


def get_uptime():

    seconds = int(time.time() - START_TIME)

    days = seconds // 86400
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60

    return f"{days}d {hours}h {minutes}m"


def database_ok():

    try:
        connection = sqlite3.connect("data/memory.db")
        connection.execute("SELECT 1")
        connection.close()
        return True

    except Exception:
        return False


def provider_status():

    return {
        provider: "Available"
        for provider in AI_PROVIDER_ORDER
    }


def get_health(bot):

    return {
        "version": config["version"],
        "build": config["build"],
        "uptime": get_uptime(),
        "servers": len(bot.guilds),
        "users": sum(g.member_count for g in bot.guilds),
        "latency": round(bot.latency * 1000),
        "database": database_ok(),
        "providers": provider_status()
    }