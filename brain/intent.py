from enum import Enum


class Intent(Enum):
    USER_INFO = "USER_INFO"
    SERVER_INFO = "SERVER_INFO"
    CHANNEL_INFO = "CHANNEL_INFO"
    BOT_INFO = "BOT_INFO"
    CONVERSATION = "CONVERSATION"
    MEMORY = "MEMORY"
    MODERATION = "MODERATION"
    AI_CHAT = "AI_CHAT"


def detect(prompt: str):

    prompt = prompt.lower()

    if any(word in prompt for word in [
        "username",
        "nickname",
        "avatar",
        "profile",
        "user id",
        "joined",
        "role"
    ]):
        return Intent.USER_INFO

    if any(word in prompt for word in [
        "server",
        "guild",
        "owner",
        "member count"
    ]):
        return Intent.SERVER_INFO

    if any(word in prompt for word in [
        "channel",
        "topic",
        "slowmode"
    ]):
        return Intent.CHANNEL_INFO

    if any(word in prompt for word in [
        "your name",
        "who are you",
        "version",
        "ping"
    ]):
        return Intent.BOT_INFO

    if any(word in prompt for word in [
        "kick",
        "ban",
        "mute",
        "timeout"
    ]):
        return Intent.MODERATION

    if any(word in prompt for word in [
        "remember",
        "forget"
    ]):
        return Intent.MEMORY

    return None