import re
from telethon import events, Client
from info import ADMINS, TARGET_CHANNEL

@client.on(events.NewMessage(chat=TARGRT_CHANNEL))
async def file_del(x):
   d=0
     if x.media and hasattr(x.media, "document"):
         name = x.file.name
         if not re.search("(?i)hindi", name):
             await x.delete()
             d += 1

   await e.reply(f"Successfully deleted {d} non Hindi Files")
   print(f"Deleted Total {d} files")
