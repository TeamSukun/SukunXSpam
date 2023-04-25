import config
from SUKUNXSPAM import BOT0, SUDOERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
 
hl = config.CMD_HNDLR
 
HELP_PIC = "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"

SUKUN_HELP = "┏━━━━━━━━━━━━━━━━━⊱\n┠ 🫧 sᴜᴋᴜɴxsᴘᴀᴍ ᴄᴍɴᴅs ❄️\n"
 
SUKUN_HELP += f"┠━━━━━━━━━━━━━━━━━⧫\n"

SUKUN_HELP += f"┠ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧\n"

SUKUN_HELP += f"┠     ┠━━━⊱ `!ping` - to check ping\n┠     ┠━━━⊱ `!alive` - to check bot alive/version.\n┠     ┠━━━⊱ `!restart` - to restart all spam bots \n┠     ┠━━━⊱ `!addecho` - to addecho \n┠     ┠━━━⊱ `!rmecho` - To remove Echo \n┠     ┠━━━⊱ `!addsudo` - To add sudo user \n┠     ┗━━━⊱ `!delsudo` to delete from sudolist\n"
 
SUKUN_HELP += f"┠ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n"

SUKUN_HELP += f"┠     ┗━━━⊱ `!leave` - to leave public/private channel/groups\n"
 
SUKUN_HELP += f"┠ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n"

SUKUN_HELP += f"┠     ┠━━━⊱ `!raid` - to raid\n┠     ┠━━━⊱ `!replyraid` - to active reply raid\n┠     ┠━━━⊱ `!dreplyraid` - to de-active reply raid\n┠     ┠━━━⊱ `!spam` - this cmd use for Normal spam\n┠     ┠━━━⊱ `!bigspam` - this cmd use for big spam\n┠     ┠━━━⊱ `!bspam` - this cmd use for spamming on someone birthday!!\n┠     ┗━━━⊱ `!delayspam` - this cmd use for delay spam\n"

SUKUN_HELP += f"┠━━━━━━━━━━━━━━━━━⧫\n┠ !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n"

SUKUN_HELP += f"┠━━━━━━━━━━━━━━━━━⧫\n© @TeamSukun \n┗━━━━━━━━━━━━━━━━━⊱\n"


@BOT0.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(event):               
    if event.sender_id in SUDOERS:
       TeamSukunbuttons = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/TeamSukun"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/sukunsupports")]]
       await BOT0.send_file(event.chat_id, HELP_PIC, caption=SUKUN_HELP, buttons=TeamSukunbuttons) 
