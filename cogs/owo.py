import discord
from discord import app_commands
from discord.ext import commands
import config


class Owo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('owo command loaded!')

    @app_commands.command(name="owo", description="owo")
    async def nano(self, interaction: discord.Interaction):
        await interaction.response.send_message('owo') 

async def setup(bot):
    await bot.add_cog(Owo(bot), guilds=[discord.Object(id=config.GUILD_ID)])