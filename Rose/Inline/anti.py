from Rose import *
from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

supunm = """
🥳╖ ❬ م2 ❭ 1⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
════════ ××× ════════ٴ
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐒╖ غبي
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤡╖ فرسه
💬╢ تاج للفرسات
📎╜ مسح الفرسات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين 
📎╜ مسح المتزوجين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ بيستي 
💬╢ تاج للبيست
📎╜ مسح البيستيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
"""

@app.on_callback_query(filters.regex("_anl"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunm,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunmascv = """
🥳╖ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
════════ ××× ════════ٴ
🐣╖ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💢╖ رقاصه 
💬╢ تاج للرقاصات
📎╜ مسح الرقاصات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐒╖ مهزء
💬╢ تاج للمهزئين
📎╜ مسح المهزئين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐕╖ فاشل
💬╢ تاج للفشله
📎╜ مسح الفشله
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐰╖ دكري
💬╢ تاج للدكور
📎╜ مسح الدكور
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤡╖ قطتي
💬╢ تاج للقطط
📎╜ مسح القطط
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ حبيبي
💬╢ تاج للحبايب 
📎╜ مسح الحبايب
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ خاين
💬╢ تاج للخونه
📎╜ مسح الخونه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ خاينه
💬╢ تاج للخاينين 
📎╜ مسح الخاينين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ عبيط
💬╢ تاج للعبط
📎╜ مسح العبط
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ متخزوق 
💬╢ تاج للمتخزوقين
📎╜ مسح المتخزوقين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·
"""
@app.on_callback_query(filters.regex("_anss"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmascv,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 

close = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('« العودة', callback_data='_bvk')
        ], 
        [
            InlineKeyboardButton( 
                text="اضف البوت الي مجموعتك ✅",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",)   
        ]], 
)    

asuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "اوامر التسليه 2️⃣", callback_data="_anssx"
                ),           
            InlineKeyboardButton
                (
                    "اوامر التسليه 1️⃣", callback_data="_anl"
                )
        ],
        [
            InlineKeyboardButton('القائمه الرئيسيه 0️⃣', callback_data='bot_commands')
        ], 
        [
            InlineKeyboardButton( 
                text="اضف البوت الي مجموعتك ✅",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",)
        ], 
    ]
)


supunmascvs = """
◍ اهلا بك فى اوامر التسليه
√"""


@app.on_callback_query(filters.regex("_bvk"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmascvs,
        reply_markup=asuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 
