from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
from discord.ext.commands.errors import CheckFailure
import utility.checkaddress
import utility.getaddress
import scholar_data
import discord
from discord.ext import commands
from datetime import datetime


class ScholarStatus(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command()
    #add commands.has_any_role
    async def status(self,ctx):
        address=utility.getaddress.get_ronin_address(ctx.author)
        if address is None:
            await ctx.send("Cannot find address")
            return
        try:
            data = scholar_data.getdata(address)
        except ConnectionError:
            await ctx.send("Cannot Connect to the API")
            return

        dt_object = datetime.fromtimestamp(int(data["last_claim_timestamp"]))

        embeds = discord.Embed(
            title = str(ctx.author)+ "Information",
            description = ctx.author.mention
        )

        embeds.add_field(name="Total SLP",value = data["total_slp"], inline=True)
        embeds.add_field(name="Claimed SLP",value = data["ronin_slp"], inline=True)
        embeds.add_field(name="Unclaimed SLP",value = data["in_game_slp"], inline=True)
        embeds.add_field(name="Last claimed SLP",value = dt_object, inline=True)

        await ctx.send(embed=embeds)

    
    @commands.command()
    async def status(self,ctx,mention):
        var = str(mention)[3:len(str(mention))-1]
        user = await self.client.fetch_user(int(var))

        address=utility.getaddress.get_ronin_address(str(user))
        if address is None:
            await ctx.send("Cannot find address")
            return
        try:
            data = scholar_data.getdata(address)
        except ConnectionError:
            await ctx.send("Cannot Connect to the API")
            return

        dt_object = datetime.fromtimestamp(int(data["last_claim_timestamp"]))

        embeds = discord.Embed(
            title = str(ctx.author)+ "Information",
            description = mention
        )

def setup(client):
    client.add_cog(ScholarStatus(client))