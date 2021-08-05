from requests.exceptions import ConnectionError
from utility.checkaddress import is_valid_address
from utility.getaddress import get_ronin_address
from utility.getSLPPrice import get_slp_data
import scholar_data
import discord
from discord.ext import commands
from datetime import datetime


class ScholarStatus(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command()
    #add commands.has_any_role
    async def status(self,ctx,target=None):
        address=get_ronin_address(ctx.author)
        
        if(target is None):
            if (address is None) :
                await ctx.send("Cannot find address")
                return
        elif (is_valid_address(target)):
            address=target
        else:
            await ctx.send("invalid address")
            return

        try:
            data = scholar_data.getdata(address)
        except ConnectionError:
            await ctx.send("Cannot Connect to the API")
            return

        dt_object = datetime.fromtimestamp(int(data["last_claimed_item_at"]))

        embeds = discord.Embed(
            title = str(ctx.author)+ " Information",
            description = ctx.author.mention
        )

        embeds.add_field(name="Total SLP",value = data["total"], inline=False)
        embeds.add_field(name="PHP",value = "₱"+str(data["total"]*get_slp_data()["smooth-love-potion"]['php']), inline=True)
        embeds.add_field(name="USD",value = "$"+str(data["total"]*get_slp_data()["smooth-love-potion"]['usd']), inline=True)
        embeds.add_field(name="Last claimed SLP",value = dt_object.strftime("%x"), inline=False)
        
        await ctx.send(embed=embeds)

    
def setup(client):
    client.add_cog(ScholarStatus(client))