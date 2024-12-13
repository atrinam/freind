import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class KNBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"در حال راه اندازی ربات")
        super().__init__(
            "KNMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<blockquote><b>{self.mention} ربات فعال شد :</b><u>\n\nشناسه : <code>{self.id}</code>\nنام : {self.name}\nنام کاربری : @{self.username} </b></blockquote>",
            )
        except:
            LOGGER(__name__).error(
                "ربات نمیتواند به گروه لاگ دسترسی پیدا کند. لطفا ربات را به کانال لاگ اضافه کرده و ادمین کنید!"
            )
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("start", "🤖 شروع کار با ربات"),
                        BotCommand("help", "📚 راهنمای دستورات"),
                        BotCommand("ping", "📡 بررسی وضعیت ربات"),
                        BotCommand("play", "▶️ پخش موزیک"),
                        BotCommand("vplay", "🎥 پخش ویدیو"),
                        BotCommand("playlist", "📋 لیست پخش"),
                        BotCommand("skip", "⏭️ رد کردن"),
                        BotCommand("pause", "⏸️ توقف موقت"),
                        BotCommand("resume", "▶️ ادامه پخش"),
                        BotCommand("stop", "⏹️ توقف پخش"),
                        BotCommand("shuffle", "🔀 پخش تصادفی"),
                        BotCommand("seek", "⏩ جلو/عقب بردن"),
                        BotCommand("reboot", "🔄 راه اندازی مجدد"),
                        BotCommand("settings", "⚙️ تنظیمات"),
                        BotCommand("stats", "📊 آمار ربات"),
                        BotCommand("sudolist", "👥 لیست سودو"),
                        BotCommand("lyrics", "📝 متن آهنگ"),
                        BotCommand("queue", "📝 صف پخش"),
                        BotCommand("clean", "🧹 پاکسازی"),
                        BotCommand("auth", "👤 کاربر مجاز"),
                        BotCommand("unauth", "🚫 لغو کاربر مجاز"),
                        BotCommand("block", "🚫 مسدود کردن"),
                        BotCommand("unblock", "✅ رفع مسدودی"),
                        BotCommand("blacklist", "⚠️ لیست سیاه"),
                        BotCommand("whois", "👤 اطلاعات کاربر"),
                        BotCommand("gbans", "🚫 لیست گلوبال بن"),
                    ]
                )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("لطفاً ربات را در گروه لاگ ادمین کنید")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"ربات موزیک {self.name} با موفقیت راه اندازی شد")
