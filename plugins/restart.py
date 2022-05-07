from pyrogram import Client

@Client.on_message(filters.command(restart))
async def restart(bot, message):
       a = await message.reply('Restarting... this may take some time.')
       await bot.restart()
       await a.delete()
       await message.reply('Restarted Successfully')
