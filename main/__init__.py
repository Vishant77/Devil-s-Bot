#Github.com/Vasusen-code

from pyrogram import Client
import os

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from .decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = int(os.environ.get("API_ID", "9126459"))
API_HASH = os.environ.get("API_HASH", "238c912d48a9ec0d0e8b05738f358ffc")
BOT_TOKEN = os.environ.get("BOT_TOKEN","5772657254:AAF2FlImkbFvlIsEVQr4QE_3go3Bi-cKWpk")
SESSION = str(os.environ.get("SESSION",'BQC9PFsX1DZk77OV0gAZp-xpOJR9HFiwDuRIpJ74USu7u9z30f-iBoi_h3KWEYNXs7PGB86l9vWkW32u6JWsPxtzafxtx9v4On2dk2_is7gnDM2rLr2wQ-G36WNKJST1Tap7pbWc7ttdavCgIzQeIVX__SwVFitwolewfNDWt5UrRAXbCeTuS4tYBbqEdEEN2D27OY9uvy8cmnlDbhLwkp15C-gVKKnNXZUiZhYz5Y-fURM4pz-Zx-yrk14nudCoIZTyqDyU1jw7ath2zLVNe2H_-aNLX6YOvavGm2j_OXp2SkfyFEnqlOSQhKkrgE5qVvyGUIaZ_l96BE6EO37nu3WTLH5jRAA'))
AUTH = int(os.environ.get("BOT_OWNER", "746480452"))
FORCESUB = config("FORCESUB",'Joint0T')


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
