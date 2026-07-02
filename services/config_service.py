import os

from config import (
    AI_PROVIDER_ORDER,
    DISCORD_PREFIX
)

from version import (
    VERSION,
    BUILD,
    MODE
)


def get():

    return {

        "version": VERSION,

        "build": BUILD,

        "mode": MODE,

        "prefix": DISCORD_PREFIX,

        "providers": AI_PROVIDER_ORDER,

        "debug": MODE == "development"
    }


def is_production():

    return MODE == "production"


def is_development():

    return MODE == "development"