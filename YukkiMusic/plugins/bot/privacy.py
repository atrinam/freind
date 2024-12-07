from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from YukkiMusic import app

TEXT = f"""
🔒
سلام!  
  هدف ما این است که شما با خیال راحت از خدمات ما استفاده کنید و مطمئن باشید که حریم خصوصی شما برای ما در اولویت است

با تشکر از اعتماد شما  
تیم رینبو"""


@app.on_message(filters.command("privacy" ,prefixes=["", "/"]))
async def privacy(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("View Privacy Policy", url="https://t.me/MUSICPLAYER_IRANIAN")]]
    )
    await message.reply_text(
        TEXT,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )

