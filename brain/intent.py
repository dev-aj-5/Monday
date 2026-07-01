from enum import Enum
import re


class Intent(Enum):
    USER_INFO = "USER_INFO"
    SERVER_INFO = "SERVER_INFO"
    CHANNEL_INFO = "CHANNEL_INFO"
    BOT_INFO = "BOT_INFO"
    CONVERSATION = "CONVERSATION"
    MEMORY = "MEMORY"
    MODERATION = "MODERATION"
    AI_CHAT = "AI_CHAT"
    TOOL = "TOOL"


def detect(prompt: str):

    prompt = prompt.lower()

    # ==================================================
    # Memory (check first)
    # ==================================================

    if any(word in prompt for word in [
        "remember",
        "forget",
        "do you remember",
        "favorite"
    ]):
        return Intent.MEMORY

    # ==================================================
    # Moderation (before Channel Info)
    # ==================================================

    if any(word in prompt for word in [

        "kick",
        "ban",
        "unban",
        "timeout",
        "mute",
        "purge",
        "clear messages",

        "warn",
        "warnings",
        "clear warnings",

        "set log channel"
    ]):
        return Intent.MODERATION

    # ==================================================
    # User Info
    # ==================================================

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

    # ==================================================
    # Server / Analytics
    # ==================================================

    if any(word in prompt for word in [

        "server",
        "guild",
        "owner",
        "member count",

        "who talks the most",
        "who talked the most",
        "most active",
        "most messages",
        "activity",
        "chat activity",
        "top chatter",

        "summary",
        "summarize",
        "chat summary",
        "summarize chat",
        "summarize this chat",
        "summarize today's chat",

        "server activity",

        "pinned",
        "pins",
        "pinned messages",

        "poll",
        "vote",
        "create poll",

        "create text channel",
        "create voice channel",

        "lock channel",
        "unlock channel"

    ]):
        return Intent.SERVER_INFO

    # ==================================================
    # Channel Info
    # ==================================================

    if any(word in prompt for word in [
        "channel topic",
        "topic",
        "slowmode"
    ]):
        return Intent.CHANNEL_INFO

    # ==================================================
    # Bot Info
    # ==================================================

    if any(word in prompt for word in [
        "your name",
        "who are you",
        "version",
        "ping"
    ]):
        return Intent.BOT_INFO

    # ==================================================
    # Conversation
    # ==================================================

    if any(word in prompt for word in [
        "previous messages",
        "earlier",
        "history",
        "last time",
        "remember our conversation"
    ]):
        return Intent.CONVERSATION

    # ==================================================
    # Calculator
    # ==================================================

    math_patterns = [

        r"^\s*[0-9+\-*/().\s]+\s*$",

        r"what('?s| is)?\s+[0-9+\-*/().\s?]+$",

        r"calculate\s+[0-9+\-*/().\s]+",

        r"solve\s+[0-9+\-*/().\s]+"

    ]

    if any(
        re.fullmatch(pattern, prompt)
        for pattern in math_patterns
    ):
        return Intent.TOOL

    # ==================================================
    # Tools
    # ==================================================

    tool_patterns = [

        "generate uuid",
        "generate a uuid",
        "create uuid",
        "create a uuid",

        "flip a coin",

        "roll d",
        "roll a d",

        "random number",

        "what time is it",
        "current time",

        "today's date",
        "what's today's date",
        "what is today's date",

        "wiki",
        "wikipedia",

        "github",
        "repository",
        "repo",

        "weather",
        "forecast",

        "search"
    ]

    if any(pattern in prompt for pattern in tool_patterns):
        return Intent.TOOL

    # ==================================================
    # Default
    # ==================================================

    return Intent.AI_CHAT