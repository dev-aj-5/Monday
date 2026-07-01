from enum import Enum

from click import prompt


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

    # ----------------------------
    # User Info
    # ----------------------------

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

    # ----------------------------
    # Server Info
    # ----------------------------

    if any(word in prompt for word in [
    "server",
    "guild",
    "owner",
    "member count",

    # Analytics
    "most active",
    "who talked the most",
    "most messages",
    "active members",
    "chat summary",
    "summarize chat",
    "summarize today's chat",
    "server activity" ,
    "summarize",
    "summary",
    "summarize today's chat",
    "summarize this chat",
    "pinned",
    "pins",
    "pinned messages",
    "create poll",
    "poll",
    "vote",
    "create text channel",
    "create voice channel",
    "lock channel",
    "unlock channel"
]):
        return Intent.SERVER_INFO

    # ----------------------------
    # Channel Info
    # ----------------------------

    if any(word in prompt for word in [
        "channel",
        "topic",
        "slowmode"
    ]):
        return Intent.CHANNEL_INFO

    # ----------------------------
    # Bot Info
    # ----------------------------

    if any(word in prompt for word in [
        "your name",
        "who are you",
        "version",
        "ping"
    ]):
        return Intent.BOT_INFO

    # ----------------------------
    # Conversation
    # ----------------------------

    if any(word in prompt for word in [
        "previous messages",
        "earlier",
        "history",
        "last time",
        "remember our conversation"
    ]):
        return Intent.CONVERSATION

    # ----------------------------
    # Memory
    # ----------------------------

    if any(word in prompt for word in [
        "remember",
        "forget",
        "what's my",
        "what is my",
        "tell me my",
        "do you remember"
    ]):
        return Intent.MEMORY

    # ----------------------------
    # Moderation
    # ----------------------------

    if any(word in prompt for word in [

    "kick",
    "ban",
    "timeout",
    "mute",
    "unban",
    "purge",
    "clear messages",
    "warn",
    "warnings",
    "clear warnings",
    "set log channel",

]):
        return Intent.MODERATION
    

# ----------------------------
# Tool Detection
# ----------------------------
    import re
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
    
    tool_patterns = [

    "generate uuid",
    "generate a uuid",
    "create uuid",
    "create a uuid",

    "flip a coin",

    "roll a d",
    "roll d",

    "random number",

    "what time is it",
    "current time",

    "what's today's date",
    "what is today's date",
    "today's date" 

]

    internet_patterns = [

    "wiki",
    "wikipedia",

    "github",
    "repository",
    "repo",

    "weather",
    "forecast",

    "search"

]
    
    all_patterns = tool_patterns + internet_patterns

    if any(pattern in prompt for pattern in all_patterns):
     return Intent.TOOL
    
    # ----------------------------
    # Default
    # ----------------------------

    return Intent.AI_CHAT