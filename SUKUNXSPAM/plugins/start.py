import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from SUKUNXSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    SUKUN_IMG = ALIVE_IMG
else:
    SUKUN_IMG = "https://te.legra.ph/file/500a7e36b22cad6459226.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "SUKUNXSPAM"

OWNER_ID = config.OWNER_ID

Sukun_Button = [
        [
        Button.url("⍟ Cʜᴀɴɴᴇʟ ⍟", "https://t.me/TeamSukun"),
        Button.url("⍟ Sᴜᴘᴘᴏʀᴛ ⍟", "https://t.me/sukunsupports")
        ],
        [
        Button.url("⍟ ѕυкυη χ мυѕι¢ ⍟", "https://t.me/sukunmusicrobot")
        ],
        [
        Button.url("⍟ Rᴇᴘᴏ ⍟", "https://github.com/TeamSukun/SukunXSpam")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[͢ ̶̶ͥ ̶ ̶ͣ ͓ ̶͓ͫ➳⃝😻𝐊εεᴘ Lᴀᴜɢʜɪɴɢ 『 🇮🇳 』➻💕](tg://user?id={2057416872})"
        SUKUN_ON = f"""
ʜᴇʏ  {mention}
┏━━━━━━━━━━━━━━━━━⊱
┠ ᴛʜɪs ɪs sᴜᴋᴜɴ sᴘᴀᴍ ʙᴏᴛ 🫢
┠━━━━━━━━━━━━━━━━━⧫
┠ 😻 ᴏᴡɴᴇʀ 🫧
┠     ┗━⊱ {myOwner}
┠ 🙈 ʟᴏᴠᴇ ❤️
┠     ┗━⊱ {mention}
┠ 💻 ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ 💸
┠     ┗━⊱ {creator}
┠━━━━━━━━━━━━━━━━━⧫
┠ ᴄᴍɴᴅs ɪɴ  ʙᴏᴛ ( /help )
┠     ┠━━━⊱ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂
┠     ┠━━━⊱ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂
┠     ┗━━━⊱ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳
┠━━━━━━━━━━━━━━━━━⧫
┠  || © @TeamSukun ||
┗━━━━━━━━━━━━━━━━━⊱

⍟ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ.
⍟ ᴀʟsᴏ ᴍᴜsᴛ ᴛʀʏ ᴏᴜʀ ᴇᴅɪᴛᴇᴅ ᴍᴜsɪᴄ ʙᴏᴛ.
⍟ ᴘᴏᴡᴇʀᴇᴅ ʙʏ {myOwner}
    """
        await e.client.send_file(e.chat_id, SUKUN_IMG, caption=SUKUN_ON, buttons=Sukun_Button)
