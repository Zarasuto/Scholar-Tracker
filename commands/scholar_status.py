from requests.exceptions import ConnectionError
from utility.checkaddress import is_valid_address
from utility.getSLPPrice import get_slp_data
import sqlscripts
import scholar_data
import discord
from discord.ext import commands
from datetime import datetime


class ScholarStatus(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command(brief= "Shows the current earnings of a scholar")
    #add commands.has_any_role
    async def status(self,ctx):
        sql_scholar_data = sqlscripts.get_scholar_data(str(ctx.author)) #try to get data of the author
        if(len(sql_scholar_data)==0):
            await ctx.send("There is no such record in the database")
            return

        try:
            data = scholar_data.getdata(sql_scholar_data[0][1])
        except ConnectionError:
            await ctx.send("Cannot Connect to the API")
            return

        dt_object = datetime.fromtimestamp(int(data["last_claim_timestamp"]))

        embeds = discord.Embed(
            title = str(sql_scholar_data[0][0])+ " Information",
            description = str(sql_scholar_data[0][1])
        )
        embeds.add_field(name="Earned SLP",value = str(data["in_game_slp"]*sql_scholar_data[0][2])+" SLP", inline=False)
        embeds.add_field(name="Total SLP", value = str(data["in_game_slp"])+" SLP",inline= True)
        embeds.add_field(name="Cut", value = str(sql_scholar_data[0][2]*100)+"%",inline= True)
        embeds.add_field(name = chr(173), value = chr(173))
        embeds.add_field(name="PHP",value = "₱"+str(data["in_game_slp"]*get_slp_data()["smooth-love-potion"]['php']*sql_scholar_data[0][2]), inline=True)
        embeds.add_field(name="USD",value = "$"+str(data["in_game_slp"]*get_slp_data()["smooth-love-potion"]['usd']*sql_scholar_data[0][2]), inline=True)
        embeds.add_field(name="Last claimed SLP",value = dt_object.strftime("%x"), inline=False)
        
        await ctx.send(embed=embeds)

    @commands.command(brief = "Shows the current mmr of the scholar", description = " Shows the current mmr of the scholar, it can also display the mmr of fellow scholars using his/her address")
    async def mmr(self,ctx,target=None):
        sql_scholar_data=""

        if(target is None): #Check if there is no additional argument
            sql_scholar_data = sqlscripts.get_scholar_data(str(ctx.author)) #try to get data of the author
            if(len(sql_scholar_data)==0):
                await ctx.send("There is no such record in the database")
                return
        elif (is_valid_address(target)): 
            sql_scholar_data = sqlscripts.get_scholar_data(str(target)) #try to get data of address
            if(len(sql_scholar_data)==0):
                await ctx.send("There is no such record in the database")
                return
        else:
            await ctx.send("invalid address")
            return
            
        try:
            data = scholar_data.getdata(sql_scholar_data[0][1])
        except ConnectionError:
            await ctx.send("Cannot Connect to the API")
            return
        
        embeds = discord.Embed(
            title = str(sql_scholar_data[0][0])+ " mmr",
            description = str(sql_scholar_data[0][1])
        )

        embeds.add_field(name = "MMR ", value = str(data["mmr"]), inline=True)
        embeds.add_field(name = "Rank ", value = str(data["rank"]), inline=True)

        await ctx.send(embed=embeds)

def setup(client):
    client.add_cog(ScholarStatus(client))