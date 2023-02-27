#Github.com/Vasusen-code

from pyrogram import Client
import os

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from .decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = int(os.environ.get("API_ID", "23365392"))
API_HASH = os.environ.get("API_HASH", "fffdba007ae9e02207be11b8d8d3f2a8")
BOT_TOKEN = os.environ.get("BOT_TOKEN","5996900120:AAFD2N1HnG2h1HcI2QN8tF6oaai9vU_OE_c")
SESSION = str(os.environ.get("SESSION",'BQB_udLh8F_G2kVnpNqzMPZExQBa9-itL4K5w0c7S8Fgzpi603a-10lCdt6O046DqO98Dd3Apw24VvwRXlpSGS812P1a5qoluacWlQ-Wea5EhEYXJUfwTcFIRucvH7DbdnGRqgxcajZVjQS1lxnN2byY0Fj771XgxTBx_rBBMPBAnWjTsGaPZP6_5gw1x-PzCUQVGjtJ4IREkkJJJLS8tFMU1g1V0-j2wMa2GeY2Ep6cWh7sc8l3S7P-DP0-q_6cvgcR3oDPVXMFxkWGbwlyBZIX-9_-COMJ5KbGDklZf4udQyNTjbQ__Q63yXLo5EdKiIDpT-LolNm7nQ3-PFbGKtP9AAAAAVcs6eMA'))
AUTH = int(os.environ.get("BOT_OWNER", "5757528547"))
FORCESUB = config("FORCESUB",'joint0t')


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
