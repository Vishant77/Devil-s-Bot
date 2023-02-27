#Github.com/im-Rudraa332

import os
from .. import Bot
from telethon import events, Button
from pyrogram import filters,Client
async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("✅ Thumbnail", data="set"),
                               Button.inline("❌ Remove Thumbnail", data="rem")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/bot_channelv1")]])

#------------------------------------------------------>
from pyrogram import Client
from pyrogram.types import Message

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)

import random
import time
import aiofiles
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import asyncio
import traceback
import string

HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **Save restricted bot**.

**I can forward restricted content of any group/channel simply**
Send Me A Link Of Your Channel\nIf You Have Private Channel,Send Me Invite #Link First.

"""

from .. import bot

@bot.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    bot = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with bot.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me An image for Thumbnail")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Thumbnail Accepted!")
        
@bot.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    bot = event.client            
    await event.edit('Trying...')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Tumbnail Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  

@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
        await cmd.reply_text(
            HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
            disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
                [
                    [
                         InlineKeyboardButton("✅ Thumbnail", callback_data="set"),
                         InlineKeyboardButton("❌ Remove Thumbnail", callback_data="rem")
                    ],
                    [
                        InlineKeyboardButton("How To Use", url="https://youtu.be/_mdB1L_0Q28")
                    ],
                     [
                        InlineKeyboardButton("Support Group", url="https://t.me/Joint0T"),
                        InlineKeyboardButton("Bots Channel", url="https://t.me/bot_channelv1")
                     ]
                ]
            )
        )

