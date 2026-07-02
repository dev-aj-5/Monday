from config import MODE
from version import VERSION


def status():

    return {
        "status": "online",
        "version": VERSION,
        "mode": MODE
    }