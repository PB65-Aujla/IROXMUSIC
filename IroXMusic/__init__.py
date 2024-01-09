from IroXMusic.core.bot import Irop
from IroXMusic.core.dir import dirr
from IroXMusic.core.git import git
from IroXMusic.core.userbot import Userbot
from IroXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Irop()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
