import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import http.client
import requests
import pyshorteners as ps
#import tracemalloc
#tracemalloc.start()

TOKEN = 'OTgyNDMwOTA4MjgxOTMzODY1.GlFwt4.iQH-4dyZGSk8ip6ZA5RPQ9rOeRVmX_iU-OvMvI'

intents=intents=discord.Intents.all()#for member joining/leaving

#client and bot
client = commands.Bot(command_prefix='!',  help_command=None)

#client = discord.Client()
bot = commands.Bot(command_prefix='.', intents=intents)

#get channel_name
channel_name_for_bot  = 'verify'


#Makes sure Bot is Getting Response
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


#Commands -- !verify, !help, !create, 'Hello', 'Bye'
@client.event
async def on_message(msg):
    username = str(msg.author).split('#')[0]
    content = str(msg.content)
    channel = str(msg.channel.name)


    if msg.author == client.user:
        return
    #if content.lower() == "help" or content.lower() == "!help":
    #   await msg.channel.send(f"```Step 1: Begin by typing !create to create the verification channel.\nStep 2: Add the Verification Bot to the 'Verify' channel that has just been created.\nStep 3: Begin typing !verify to begin the verification process!```")
    #    return
    #if msg.channel.name == channel_name_for_bot:
    if content.lower() == 'thanks' or content.lower() == 'thank you' or content.lower() == 'thank':
        await msg.channel.send(f"You Welcome {username}!")
        return
    elif content.lower() == "help" or content.lower() == "!help":
        await msg.channel.send(f'```Step 1: Use the link to authorize the bot onto the server: https://discord.com/api/oauth2/authorize?client_id=982430908281933865&permissions=534992386160&scope=bot\nStep 2: Go to the channel where you want the bot added and click the gear icon next to the channel. Go to *Permissions* and then *Add Members and Roles*\nStep 3: Search for *Chat Bot* and Add!\nStep 4: Type !verify to begin the verification process.```')
        return
    elif content.lower() == '!verify':
        print("Verification Sent!")
        CLIENT_ID = 'SERVER_4R3QUQRNQOSK9TOTWHD7Q2'
        cs = 'g_zsgbW00owFeQHKmfyXP7p6_iUJ9U797_iThf19AsP-jeZu7DWeGqJ.V3aLRRzm'
        headers = {'client-id': 'SERVER_4R3QUQRNQOSK9TOTWHD7Q2', 'client-secret': cs , 'Content-Type' : 'application/json' }
        response = requests.post('https://core.human-id.org/v0.0.3/server/users/web-login', headers=headers)
        return_url = response.json()['data']['webLoginUrl']
        short_url = ps.Shortener().tinyurl.short(return_url)
        await msg.channel.send(short_url)
        #msg.author gets new role when verification is complete

        #if response.json()['success'] == True:
        #
        #print(headers)
        #response2 =  requests.post('https://core.human-id.org/v0.0.3/server/users/exchange', headers=headers)
        #return_value = response2.json()
        #print(response2.json())
        #print(return_value['success'])
        #if return_value['success'] == True:
        #    et = return_value['exchangeToken']
        #    print('http://18.225.5.208:8000/success_bot?et=' + et)
        #else:
        #    reason = str(response2.reason)
        #    reason = reason.replace(' ', '')
        #    fail_url = ('http://18.225.5.208:8000/failure_bot?code=' + str(response2.status_code) + '&message=' + reason)
        #    print(fail_url)
        #await msg.channel.send(f"https://bit.ly/3A5b5bW")
        return
    elif content.lower() == '!create':
        if  get(msg.guild.text_channels, name="verify"):
            await msg.channel.send(f"Verification Channel already created")
        else:
            await msg.guild.create_text_channel('verify')
            return
        # https://stg-web-login.human-id.org/login?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdXJwb3NlIjoid2ViLWxvZ2luL3JlcXVlc3QtbG9naW4tb3RwIiwic2lnbmF0dXJlIjoiZDVmZmQyODYxY2IzZDM5YjQ5NDY5ZTg0MGNkMGJlMGU5OTIzYjY1MWJiM2EyMTYyY2RiZjBhMjZjNzQwYTAwZiIsImlhdCI6MTY1NTQzMzgyNSwiZXhwIjoxNjU1NDM0MTI1LCJzdWIiOiJTRVJWRVJfR1hJVFM3TlZZM0RETVozNVdVSDdDWCIsImp0aSI6ImQ5TFJsdzFRRXFmMG54TGJTMHRCQjlBaVFQb0lQWDVJOUpPbHlrMzdYOFRvT0xmRHdsWnE1WlBwYVJHWkxXNlUifQ.CTcjfbw5mlqUvgqPLZyxiRRRafFMbnYlyA14XE9jkU4&a=IO5T8PZH2O15N8SV&lang=en&priority_country=ID&s=w")
            #JWT TOKEN IS EXPIRED
            #step 1: connect to humanID server    so success on humanID server authenticates and give approval msg----   api connect?
            #step 2: complete verfication process ------ phone number (doesnt need to be coded)
           #step 3: change member roles          ------- Code: client_role = client.get_guild(), wait payload.member.add_roles('verified')
        return


# AS MEMEBER JOINS, MESSAGE DISPLAYING!
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(983183146910634024)
    print(member.name + " has joined the server!")
    embed=discord.Embed(
            title="Welcome "+member.name+"!",
            #description="We're so glad you're here! Type !verify to begin verification process!",
            color=discord.Color.green()
            )
    await member.send("thanks for joining")
    await channel.send(member.mention, embed=embed)
            #role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    #await client.add_roles(member, role) # Gives the role to the user
    #print("Added role '" + role.name + "' to " + member.name)
    return


# AS MEMBER LEAVES, MESSAGE DISPLAYING!
@bot.event
async def on_member_remove(member):
    print(member.name + " has left the server!")
    embed=discord.Embed(
            title="Goodbye "+member.name+"!",
            #description="Until we meet again old friend.",# A description isn't necessary, you can delete this line if you don't want a description.,
            color=discord.Color.red() # check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
            )
    await member.send("Thank you for your service!")
    return



#@client.command()
#@commands.has_guild_permissions(administrator=True)
#async def send_message(ctx, channel: discord.TextChannel, *, message: str):
#    await channel.send(message)
#    return


#Add new role
@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addRole(self, ctx, user: discord.Member, *, role: discord.Role):
    if role in user.roles:
        print("no role added")
    else:
        await user.add_roles(role)
#    role = get(member.server.roles, name="Verified")
#   await member.add_roles(member, role)
        print("should have worked")

#Execution
client.run(TOKEN)


#Links
#-----------------------------------------------------------------------------------
#https://bit.ly/3awjgD3
#https://web-login.human-id.org/login?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdXJwb3NlIjoid2ViLWxvZ2luL3JlcXVlc3QtbG9naW4tb3RwIiwic2lnbmF0dXJlIjoiZTk4YTgxZmJkM2QzNDA4NzJmY2VlZDE3YTUwYTM1MjRhM2NjNmM3MzhiOWMwNjRlYWY3YjJjZTM3MjAyMzBmNyIsImlhdCI6MTY1NDUwMDQ2NywiZXhwIjoxNjU0NTAwNzY3LCJzdWIiOiJTRVJWRVJfR1hJVFM3TlZZM0RETVozNVdVSDdDWCIsImp0aSI6Ijh5cE1GTnpNQmF4Y1Q1NWZLdXB6MUJjZndwZEZaZWI4OUxCcVlyWkRIZ3g2YTdRcEZRNndOMDNSMmJ4eTEyNHkifQ.WDlXMVFXVq-qhIZPHb_FOKfdPhATKaZ6SNcUd49P2to&a=IO5T8PZH2O15N8SV&lang=en_US&priority_country=US&s=w
#https://docs.human-id.org/web-sdk-integration-guide/example-web-sdk-integration


#Notes
#---------------------------------------------------------------------------------------
#msg.channel.send(f'Hello {username}! Type !verify to begin verification process!'i:wq
#

