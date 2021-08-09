import os


class Config:

    API_ID = int(os.environ.get("API_ID", 2870743))
    API_HASH = os.environ.get("API_HASH", "ae3b52c01ee412de9060742628296c88")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1835205769:AAGYRwkcDPY02AnMdBGWDn2yMnEpnZtSYFM")
    SESSION_NAME = os.environ.get("SESSION_NAME", "soethuya")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001548862820"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://soethuya:soethuya@cluster0.xz9fj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "1420701422").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
