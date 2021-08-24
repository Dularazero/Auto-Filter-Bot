
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("1915008911:AAEy986BDn7eHMlt-aX21qMBHnYUDp8Xyek", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("7857909", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("05324caf2f243a4fd0778c53489ed5fd", "")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("1BVtsOJgBu3GS4M6LY-3cemux52k4zlt196Wjfmal7q1wPlBY5CpzTvq1Ym4_pOpMWbvsQXKduYKHt78XxVJWdgHAq5uXE8jd0pqsZf2wIdGbJLcWD03dtvwePUJ8zYGA-SPJ7knxkU31UVvrF_uxgDGk1NG9-rssyy1-zdoewZRVn4pazaUpI7kqKGpLw8O8BXA3me2xlQL5s5QkB-cLBeGWm4uY_aKuuAxeN_gLgxvxO-L9WuP2VZXD1oJZ9AtR98NntZbPYmALS2JNBdQHL_hNvmvddVKHiY_a8KfHsBfQDOsUZ8mapePko3Kb5m4gORPqVXguTw-ukoeomH_JYTV6K70Fqk0=", "")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("-1001582512651", "")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
