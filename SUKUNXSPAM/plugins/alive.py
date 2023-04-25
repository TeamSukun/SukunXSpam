import config
from SUKUNXSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    SUKUN_PIC = PIC
else:
    SUKUN_PIC = "https://te.legra.ph/file/500a7e36b22cad6459226.jpg"

hl = config.CMD_HNDLR


SUKUN = "┏━━━━━━━━━━━━━━━━━⊱\n┠ 🫢 sᴜᴋᴜɴxsᴘᴀᴍ ❤️\n"
SUKUN += f"┠━━━━━━━━━━━━━━━━⧫\n"
SUKUN += f"┠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** \n┠     ┗━━━⊱ `4.0.0`\n"
SUKUN += f"┠ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** \n┠     ┗━━━⊱ `{version.__version__}`\n"
SUKUN += f"┠ **ᴅᴇᴀᴅʟʏʙᴏᴛ ᴠᴇʀsɪᴏɴ** \n┠     ┗━━━⊱ `{deadlyversion}`\n"
SUKUN += f"┗━━━━━━━━━━━━━━━━━⊱\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     TeamSukunbuttons = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/TeamSukun"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/sukunsupports")], [Button.url("⍟ ʀᴇᴘᴏ ⍟", "https://github.com/TeamSukun/SukunXSpam"),  [Button.url("𖢵 ѕυкυη χ мυѕι¢ 𖢵", "https://t.me/sukunmusicrobot")]]
     await BOT0.send_file(event.chat_id, SUKUN_PIC, caption=SUKUN, buttons=TeamSukunbuttons)
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ sᴜᴋᴜɴxsᴘᴀᴍ!**") 
