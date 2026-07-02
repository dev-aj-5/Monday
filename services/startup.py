from version import (
    NAME,
    VERSION,
    CODENAME,
    AUTHOR,
    BUILD
)


def banner():

    print()
    print("=" * 55)
    print(f"{NAME} {VERSION}")
    print(f"Codename : {CODENAME}")
    print(f"Author   : {AUTHOR}")
    print(f"Build    : {BUILD}")
    print("=" * 55)
    print()

import os

from config import (
    DISCORD_TOKEN,
    GEMINI_API_KEY,
    OPENROUTER_API_KEY,
    GROQ_API_KEY
)


def check_environment():

    print("Checking environment...")

    if not DISCORD_TOKEN:
        raise RuntimeError("Missing DISCORD_TOKEN")

    providers = 0

    if GEMINI_API_KEY:
        providers += 1

    if OPENROUTER_API_KEY:
        providers += 1

    if GROQ_API_KEY:
        providers += 1

    print(f"AI Providers Available: {providers}")

    if providers == 0:
        raise RuntimeError("No AI providers configured.")

    print("Environment OK")

from services.memory_service import initialize


def initialize_services():

    print("Initializing database...")

    initialize()

    print("Database ready.")

import time

from services.metrics_service import set_startup_time

_start = time.perf_counter()


def finish():

    elapsed = time.perf_counter() - _start

    # Store startup time for metrics
    set_startup_time(elapsed)

    print()
    print("=" * 55)
    print("Monday is ready.")
    print(f"Startup Time : {elapsed:.2f}s")
    print("=" * 55)