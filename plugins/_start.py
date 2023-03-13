# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Search YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply(
        f"السلام عليكم يا  {message.from_user.first_name}!\n\n هذا بوت لتحميل فيديوهات و قوائم يوتيوب سواء بصيغة فيديو أو صوت , فقط أرسل رابط الفيديو أو قائمة التشغيل   \n "
        f"ممنوع استخدام البوت لتحميل كل ما هو حرام شرعاً , استعمله في سبيل الله \n"
        f"●/playlist_aud - <i>رابط قائمة التشغيل </i> :لتحميل القائمة في صيغة صوتية \n " 
        f"لبقية البوتات هنا \n https://t.me/ibnAlQyyim/1120 \n "
        f"تم تطويره بواسطة \n sanila"
    )
