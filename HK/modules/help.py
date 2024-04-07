from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"Hᴋ ꭙ Sᴘᴀᴍ 🫧 ʜᴇʟᴘ ᴍᴇɴᴜ ♡︎\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: Hᴋ ꭙ Sᴘᴀᴍ 🫧**"

HELP_BUTTON = [
    [
      Button.inline("✨ sᴘᴀᴍ ✨", data="spam"),
      Button.inline("✨ ʀᴀɪᴅ ✨", data="raid")
    ],
    [
      Button.inline("🦋 ᴄᴏᴍᴍᴀɴᴅs 🦋", data="extra")
    ],
    [
      Button.url("⚜️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚜️", "https://t.me/llxHKxll"),
      Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/KaisenWorld")
    ],
  [   
      Button.inline("ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅ", data="yash")
      
  ]
]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/803868e39daf8729919f8.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**»💓 ᴍᴀɪɴ ᴄᴏᴍᴍᴀɴᴅs 💓:**

**๏ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs**
  1) {hl}ᴘɪɴɢ
  2) {hl}ʀᴇʙᴏᴏᴛ
  3) {hl}sᴜᴅᴏ » ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅ
  4) {hl}ʟᴏɢs » ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅ

🍁 ▸ 𝙴𝙲𝙷𝙾 : **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ**
  1) {hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>
  2) {hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>

🍁 ▸ 𝙻𝙴𝙰𝚅𝙴 : **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}ʟᴇᴀᴠᴇ <ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ>
  2) {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ 

🍁 ▸ 𝙰𝙱𝚄𝚂𝙴 𝚂𝙿𝙰𝙼 : **oɴᴇ ᴡᴏʀᴅ ɢᴀᴀʟɪ sᴘᴀᴍ**
  1) {hl}ᴀʙᴜsᴇ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  
**© Hᴋ ꭙ Sᴘᴀᴍ 🫧**
"""



yash_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs :**

🦋 ▸ 𝙶𝙾𝙾𝙳 𝙰𝙵𝚃𝙴𝚁𝙽𝙾𝙾𝙽: **ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ɢᴀ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ɢᴀ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

🦋 ▸ 𝙶𝙾𝙾𝙳 𝙼𝙾𝚁𝙽𝙸𝙽𝙶 : **ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ɢᴍ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ɢᴍ <ᴜsᴇʀɴᴀᴍᴇ>

🦋 ▸ 𝙶𝙾𝙾𝙳 𝙽𝙸𝙶𝙷𝚃 : **ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ɢɴ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ɢɴ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

🦋 ▸ 𝙴𝙼𝙾𝙹𝙸 : **ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴇᴍᴏᴊɪ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ᴇᴍᴏᴊɪ <ᴜsᴇʀɴᴀᴍᴇ>

🦋 ▸ 𝚂𝙷𝙰𝚈𝚁𝙸 𝚁𝙰𝙸𝙳 : **sʜᴀʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

🦋 ▸ 𝙵𝙻𝙸𝚁𝚃𝙸𝙽𝙶 : **ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ғʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ғʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

🦋 ▸ 𝙱𝙸𝚁𝚃𝙷𝙳𝙰𝚈 : **ʙɪʀᴛʜᴅᴀʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>



**© Hᴋ ꭙ Sᴘᴀᴍ 🫧**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs :**

✨ ▸ 𝚁𝙰𝙸𝙳 : **ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ >
  2) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

✨ ▸ 𝚁𝙴𝙿𝙻𝚈 𝚁𝙰𝙸𝙳 : **ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʀʀᴀɪᴅ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

✨ ▸ 𝙳𝚁𝙴𝙿𝙻𝚈 𝚁𝙰𝙸𝙳 : **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴅʀʀᴀɪᴅ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ᴅʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

✨ ▸ 𝙼𝚁𝙰𝙸𝙳 : **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

✨ ▸ 𝚂𝚁𝙰𝙸𝙳 : **sʜᴀʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀɴᴀᴍᴇ>

✨ ▸ 𝙲𝚁𝙰𝙸𝙳 : **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**© Hᴋ ꭙ Sᴘᴀᴍ 🫧**
"""

spam_msg = f"""
**» sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs :**

💓 ▸ 𝚂𝙿𝙰𝙼 : **sᴘᴀᴍs ᴀ ᴍᴇssᴀɢᴇ**
  1) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ>  < 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐓𝐎 𝐒𝐏𝐀𝐌 >  (𝐘𝐎𝐔 𝐂𝐀𝐍 𝐑𝐄𝐏𝐋𝐘 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐈𝐅 𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐑𝐄𝐏𝐋𝐘 𝐓𝐇𝐀𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐀𝐍𝐃 𝐃𝐎 𝐒𝐏𝐀𝐌𝐌𝐈𝐍𝐆 )
  2) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ> < 𝐑𝐄𝐏𝐋𝐘𝐈𝐍𝐆 𝐀𝐍𝐘 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 > 

💓 ▸ 𝙷𝙰𝙽𝙶 : **sᴘᴀᴍs ʜᴀɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ ᴄᴏᴜɴᴛ**
  1) {hl}ʜᴀɴɢ <ᴄᴏᴜɴᴛ>


** © Hᴋ ꭙ Sᴘᴀᴍ 🫧**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("✨ sᴘᴀᴍ ✨", data="spam"),
                Button.inline("✨ ʀᴀɪᴅ ✨", data="raid"),
                Button.inline("✨ ᴇxᴛʀᴀ ᴄᴍᴅ ✨", data="yash")
              ],
              [
                Button.inline("🍁 ᴄᴏᴍᴍᴀɴᴅs 🍁", data="extra")
              ],
              [
                Button.url("⚜️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚜️", "https://t.me/llxHKxll"),
                Button.url("🦋 sᴜᴘᴘᴏʀᴛ 🦋", "https://t.me/KaisenWorld")
              ]
            ]
          )
    else:
        await event.answer("♡︎ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀɢ @llxHKxll" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("♡︎ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀɢ @llxHKxll", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("♡︎ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀɢ @llxHKxll", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("♡︎ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀɢ @llxHKxll", cache_time=0, alert=True)
        

@X1.on(events.CallbackQuery(pattern=r"yash"))
@X2.on(events.CallbackQuery(pattern=r"yash"))
@X3.on(events.CallbackQuery(pattern=r"yash"))
@X4.on(events.CallbackQuery(pattern=r"yash"))
@X5.on(events.CallbackQuery(pattern=r"yash"))
@X6.on(events.CallbackQuery(pattern=r"yash"))
@X7.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
@X9.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
async def help_yash(event):
     if event.query.user_id in SUDO_USERS:
         await event.edit(yash_msg,
             buttons=[[Button.inline("< Back", data="help_back"),],],
             )
     else:
         await event.answer("♡︎ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛᴀɢ @llxHKxll", cache_time=0, alert=True)
