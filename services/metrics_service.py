from collections import defaultdict
from datetime import datetime

metrics = {
    "startup_time": None,
    "commands": 0,
    "errors": 0,
    "ai_requests": 0,
    "provider_usage": defaultdict(int),
    "command_usage": defaultdict(int),
    "started": datetime.utcnow()
}


def record_command(command):

    metrics["commands"] += 1
    metrics["command_usage"][command] += 1


def record_provider(provider):

    metrics["ai_requests"] += 1
    metrics["provider_usage"][provider] += 1


def record_error():

    metrics["errors"] += 1


def set_startup_time(seconds):

    metrics["startup_time"] = seconds


def get_metrics():

    return metrics