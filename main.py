
import discord
import json
from discord.ext import commands
import os, jishaku
os.system('clear')
import requests
import aiohttp
import random 
from keep_alive import keep_alive
os.system("pip install discord-py-slash-command")
import websocket
import datetime
import asyncio
def get_prefix(client, message):
  with open('server.json', 'r')as f:
      server = json.load(f)

  return server[str(message.guild.id)]



punch_gifs = ['https://c.tenor.com/EvBn8m3xR1cAAAAM/toradora-punch.gif', 'https://images.app.goo.gl/mqvtKk4YMh3jDLnn7']
punch_names = [f'punches you']

kick_gifs = ['https://images.app.goo.gl/v3BXRTANPGBta1Nv5']
kick_names = ['kicks Aww', 'Good bye']
client = commands.Bot(command_prefix =  get_prefix , help_command=None)


intents = discord.Intents.default()
intents.members = True
client.load_extension('jishaku')


  

@client.event
async def on_ready():
  print(f'Gonna work for {len(client.users)} users')
  await  client.change_presence(status =discord.status.mobile ,activity = discord.Activity(type =discord.ActivityType.watching, name=('>help | Under Devlopment ')))
  
@client.event
async def on_member_join(member):
  print(f'{member} has joined')

@client.event
async def on_member_remove(member):
  print (f'{member} has left')

@client.event
async def on_guild_join(guild):
  with open('server.json', 'r')as f:
      server = json.load(f)

  server[str(guild.id)] = '>'
  
  with open('server.json', 'w')as f:
       json.dump(server, f, indent=4)

@client.event
async def on_guild_remove(guild):
  with open('server.json', 'r')as f:
    PermissionError 
    server = json.load(f)

  server.pop(str(guild.id))
  
  with open('server.json', 'w')as f:
       json.dump(server, f, indent=4)
  
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member :discord.Member, *, reason="No reason Provided"):
  await member.kick(reason=reason)
  em = discord.Embed(tittle='', description=f"✅ {member} has been kicked | {reason}") 
  await ctx.send(embed=em)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member :discord.Member, *, reason="No Reason Provided"):
 await member.ban(reason=reason)
 em = discord.Embed(title="", description=f"✅ {member} has been Banned | {reason}")
 await ctx.send(embed=em)

@client.command(aliases=["h"])
async def help(ctx):
  embed = discord.Embed(
     title = 'Rex Security',
     description = 'Thank you for using our bot❤️ ' 

  )
  embed.set_footer(text=f'Requested by {ctx.author}')
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/980429877641637933/981387239978336346/IMG_20220531_105200.jpg4sa')
  embed.add_field(name='<a:dot:984832896059703347> moderation', value='Shows Moderation commands', inline=False)
  embed.add_field(name='<a:dot:984832896059703347> fun', value='shows fun commands', inline=True)
  embed.add_field(name='<a:dot:984832896059703347> nsfw', value='shows nsfw info', inline=True)
  embed.add_field(name='<a:dot:984832896059703347> Ye soon',
value='soon', inline=True)
  embed.add_field(name='invite me',
value='<a:dot:984832896059703347> [Rex Security](https://dsc.gg/rex-sec)', inline=True)
  await ctx.send(embed=embed)

@client.command()
async def moderation(ctx):
  embed = discord.Embed(
     title = 'Rex Security',
     description = ''

  )
  embed.set_footer(text='Made with DEEPAK♥️') 
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/980429877641637933/981387239978336346/IMG_20220531_105200.jpg')
  embed.add_field(name='null', value='null', inline=False)
  embed.add_field(name='null', value='null', inline=True)
  embed.add_field(name='null', value='null', inline=True)
  embed.add_field(name='null',
value='null', inline=True)
  embed.add_field(name='Invite me',
value='[Invite me](https://dsc.gg/rex-sec)', inline=True)
  await ctx.send(embed=embed)

@client.command(aliases=["slowmo", "sm"])
async def slowmode(ctx,time:int):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send('This command requires ``Manage Messages``')
            return
        try:
            if time == 0:
                await ctx.send('Slowmode turned off')
                await ctx.channel.edit(slowmode_delay = 0)
            elif time > 21600:
                await ctx.send('You cannot set the slowmode above 6 hours!')
                return
            else:
                await ctx.channel.edit(slowmode_delay = time)
                await ctx.send(f'Slowmode set to {time} seconds!')
        except Exception:
            print('Hmmmm..')

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
 with open('server.json', 'r')as f:
      server = json.load(f)
   
      server[str(ctx.guild.id)] = prefix
 with open('server.json', 'w')as f:
       json.dump(server, f, indent=4)
 
 embed = discord.Embed(title = '', description = f' <:auroraTick:981392641377837066> | Server prefix set to {prefix}')
  
 embed.set_thumbnail(url='https://media.discordapp.net/attachments/980429877641637933/981387239978336346/IMG_20220531_105200.jpg')
 await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title = 'Pong!', description = f'{round(client.latency * 1000)} ms')  
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/981438437590700103/981745867973357618/9950_WumpusKeyboardSlam-gifemoji.gif')
  await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount : int):
   await ctx.channel.purge(limit=amount)
   await ctx.reply(f'<:auroraTick:981392641377837066> |purged {amount} messages')
 
@client.command()
@commands.is_nsfw()
async def nsfw(ctx):
  embed = discord.Embed(title = 'nsfw comnands', description = 'anal,pussy,cumshot,porn gif')  

  await ctx.send(embed=embed)
  
@client.command()
@commands.is_nsfw()
async def f(ctx):
 r = requests.get("https://www.reddit.com/r/nsfw/new.json?sort=hot")
 res = r.json()
 em = discord.Embed(title=f'Requested by {ctx.author}')
 em.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
 await ctx.reply(embed=em)
@client.command()
async def n(ctx):
  if ctx.channel.is_nsfw():
        embed = discord.Embed(title=f"Requested by {ctx.author}", description="")  
  async with aiohttp.ClientSession() as cs:
        async with cs.get('https://nsfw3.p.rapidapi.com/v1/results') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
    
@client.command()
async def punch(ctx):
 embed = discord.Embed(
    colour=(discord.Colour.random()), 
    description = f"{ctx.author} {(random.choice(punch_names))}"
 )  
 embed.set_image(url=(random.choice(punch_gifs)))
 
 await ctx.send(embed =embed)

@client.command()
async def kixk(ctx):
 embed = discord.Embed(
    colour=(discord.Colour.random()), 
    description = f"{ctx.author} {(random.choice(kick_names))}"
 )  
 embed.set_image(url=(random.choice(kick_gifs)))
 
 await ctx.send(embed =embed)


@client.command(aliases=["mc"])
async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f" {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

@client.command(aliases=["m"])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
 guild=ctx.guild
 mutedRole = discord.utils.get(guild.roles, name='Muted')

 if not mutedRole: 
     mutedRole = await guild.create_role(name="Muted")
   
     for channel in guild.channels:
         await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
  
 await member.add_roles (mutedRole, reason=reason)
 await ctx.send(f"Muted {member.mention} for reason {reason}")
 

@client.event
async def on_command_error(ctx, error):
  
 embed = discord.Embed(title = '', description = f'<:auroraCross:981392610851688459> | {error}')
 await ctx.send(embed=embed)

@client.command()
async def afk(ctx, reason=None):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author}, Your afk is: {reason} ")
    counter = 0
    while counter <= int(minute):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break

@client.command(aliases = ['av'])
async def avatar(ctx, *,  avamember : discord.Member=None):
    if discord.member == None:
        member = ctx.author 
        
    embed = discord.Embed(title = f"{member.name}'s avatar", color = 0x2F3136)
    embed.set_image(url = member.avatar_url)
    embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.userAvatarurl)
    await ctx.send(embed = embed)

@client.command()
async def avatr(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
            
keep_alive()      
client.run('OTgxMTI4MTc5NjgwOTQ0MTY5.G0G_m4.XEx3p-ZI5b1z-o1lctk3GacMJGa-arGGrZ4VgQ')
