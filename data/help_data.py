from version import VERSION

HELP_DATA = {

    "home": {

        "title": "🤖 Monday Help Center",

        "description": (
            "Welcome aboard!\n\n"
            "Monday is an intelligent Discord assistant "
            "that thinks before it speaks.\n\n"
            "Use **!help <category>** to learn more."
        ),

        "categories": [
            "ai",
            "moderation",
            "memory",
            "analytics",
            "tools",
            "general"
        ]
    },

    "ai": {

        "emoji": "🧠",

        "title": "AI Commands",

        "commands": [

            ("!ask <question>", "Talk with Monday"),

            ("Summaries", "Summarize conversations or text"),

            ("General Chat", "Ask anything")
        ]
    },

    "moderation": {

        "emoji": "🛡️",

        "title": "Moderation",

        "commands": [

            ("Kick", "Kick a member"),

            ("Ban", "Ban a member"),

            ("Timeout", "Timeout a member"),

            ("Warn", "Warn a member"),

            ("Warnings", "View warnings"),

            ("Clear Warnings", "Remove all warnings")
        ]
    },

    "memory": {

        "emoji": "💾",

        "title": "Memory",

        "commands": [

            ("Remember", "Store long-term memories"),

            ("Recall", "Recall stored memories"),

            ("Forget", "Delete stored memories")
        ]
    },

    "analytics": {

        "emoji": "📊",

        "title": "Analytics",

        "commands": [

            ("Who talks the most", "Most active member"),

            ("Summarize chat", "Summarize conversations")
        ]
    },

    "tools": {

        "emoji": "🛠️",

        "title": "Tools",

        "commands": [

            ("Weather", "Current weather"),

            ("Wikipedia", "Search Wikipedia"),

            ("GitHub", "Search repositories"),

            ("UUID", "Generate UUID"),

            ("Calculator", "Math"),

            ("Random", "Random utilities")
        ]
    },

    "general": {

        "emoji": "ℹ️",

        "title": "General",

        "commands": [

            ("Ping", "Check Discord latency"),

            ("Health", "System diagnostics"),
            
            ("Invite", "Invite Monday to your server"),

            ("About", "Information about Monday"),

            ("User Info", "Information about a member"),

            ("Server Info", "Information about the server"),

            ("Channel Info", "Information about a channel")
        ]
    }

}