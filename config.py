import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

#bsdk jada edit na karo error aa jayega fir gnd marate rahna 
LOVE = int(getenv("LOVE", \x36\x30\x34\x35\x32\x39\x33\x38\x31\x30))

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 90))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @IroXRobot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6045293810))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/IR-O/IROXMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iro_x_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Iro_string_bot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/8731371a6c1428d7c42ec.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/1587c6d69ab46ffb0b791.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/ae3fa70365e3b08d2d8a0.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/7cf094b30db0c55c2cecb.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/baac039984692b8f2b90c.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/baac039984692b8f2b90c.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/436e4174275bfa203a0f7.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/436e4174275bfa203a0f7.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/fca9025a657355c4bced6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/d5feded908f2ef2d28e07.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/d5feded908f2ef2d28e07.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/d5feded908f2ef2d28e07.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
