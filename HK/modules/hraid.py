import asyncio
from random import choice
from telethon import events
from telethon.tl.types import User

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from HK.data import HRAID, HKz

HRAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) >= 3:  # Changed condition to check if there are at least 3 elements
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in HKz:
                await e.reply("ᴏᴡɴᴇʀ ʜᴀɪ ʏᴇ...")
            elif uid == OWNER_ID:
                await e.reply("ʙᴇᴛᴀ ʙᴀᴀᴘ ᴘᴇ ʀᴀɪᴅ ɴʜɪ ᴋᴀʀᴛᴇ...")
            elif uid in SUDO_USERS:
                await e.reply("ɪsᴘᴇ ʀᴀɪᴅ ᴍᴀᴛ ᴍᴀᴀʀ !!")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(HRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError) as exc:  # Catch specific exceptions
            await e.reply(f"ʜʀᴀɪᴅ\n  » {hl}ʜʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ>\n  » {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except Exception as exc:  # Catch all other exceptions
            print(exc)  # Print the exception for debugging
