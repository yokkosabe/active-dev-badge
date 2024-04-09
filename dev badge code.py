import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix='*', intents=disnake.Intents.all())

TOKEN = 'your bot token' # In quotes you need to indicate token of your bot from discord developer portal

@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
   await interaction.send('test message')

bot.run(TOKEN)
