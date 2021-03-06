#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + """</code>\n
<b>Uploaded by :
@movieworldkdy

✪༺ ──•◈•─ •─  ─•◈•──༻✪

ᴀʟʟ ᴄʜᴀɴɴᴇʟs : @mwklinks
ᴏᴛᴛ ʀᴇʟᴇᴀꜱᴇ    : @mwkchannel4
ᴡᴇʙ ꜱᴇʀɪᴇꜱ      : @MWKseries
ᴛᴇᴄʜ, ꜱᴜᴩᴩᴏʀᴛ : @redbullfed

🎗️ ѕнαяє🎗️ ѕυρρσят 🎗️

❤️ Fɪʀꜱᴛ Oɴ Tᴇʟᴇɢʀᴀᴍ ❤️</b>""")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '❤️ share group with friends ❤️', url="http://t.me/share/url?url=%2A%2AHai+Bro%20%E2%9D%A4%EF%B8%8F%2C%20%2A%2A%0A__Today%20I%20Just%20Found%20Out%20A%20Movie+Group%20Which%20Uploads__%20%2A%2ARequested+Movies%20In%20Second's%2A%2A%F0%9F%A5%B0.%0A%2A%2AJσιи+Nσω%20%20%3A%20%40MOVIEWORLDKDY+👌%F0%9F%94%A5%2A%2A"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '❤️ share group with your friends ❤️', url="http://t.me/share/url?url=%2A%2AHai+Bro%20%E2%9D%A4%EF%B8%8F%2C%20%2A%2A%0A__Tohttp://t.me/share/url?url=%2A%2AHai+Bro%20%E2%9D%A4%EF%B8%8F%2C%20%2A%2A%0A__Today%20I%20Just%20Found%20Out%20A%20Movie+Group%20Which%20Uploads__%20%2A%2ARequested+Movies%20In%20Second's%2A%2A%F0%9F%A5%B0.%0A%2A%2AJσιи+Nσω%20%20%3A%20%40MOVIEWORLDKDY+👌%F0%9F%94%A5%2A%2A👌%F0%9F%94%A5%2A%2Al"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/shamilnelli"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        return
