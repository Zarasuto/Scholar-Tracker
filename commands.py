from discord.ext.commands.errors import CheckFailure
import json
import scholar_data
import discord
from discord.ext import commands
from datetime import datetime


class Commands(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    """add scholars"""
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_scholar(self,ctx,mention, address):
        #filename = 'scholars.json'
        ##entry = {name : address}
        #with open(filename,"r+") as file:
        #    data= json.load(filename)
        #    data.append(entry)
        #    file.seek(0)
        #    json.dump(data,file)
        #print(str(mention)[2,len(mention)-1])
        var = str(mention)[3:len(str(mention))-1]
        await ctx.send(str)

    @commands.command()
    async def status(self,ctx):
        embeds = discord.Embed(
            title = str(ctx.author)
        )
        await ctx.send(embed=embeds)
    
    #Checks if any of the user has no permission
    @add_scholar.error
    async def check_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Not Enough Permissions')


def setup(client):
    client.add_cog(Commands(client))