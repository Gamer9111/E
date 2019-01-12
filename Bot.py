import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '/')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'why the fuck would you join this dead but cancerous chat?')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Suffering'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '/DIO':
        await client.send_message(message.channel,'go away')
    if message.content.startswith('/Coinflip'):
        randomlist = ["Heads","Tails","Not Heads","Very Tails"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Dice'):
        randomlist = ["1","2","3","4","5","6"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Gay?'):
        randomlist = ["Yes","Big Yes","suprisingly now","somehow no"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Whogay?'):
        randomlist = ["U","cunt above","fag above the fag above u","fag below u"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/Bully '):
        await client.send_message(message.channel,'no u <@%s>'  %(message.author.id))
    if ('Bowsette ') in message.content:
       await client.delete_message(message)
    if message.content == 'MUDA MUDA MUDA MUDA':
        await client.send_message(message.channel,'https://i.imgur.com/oNcHdPX.gif')
    if message.content == 'ORA ORA ORA ORA':
        await client.send_message(message.channel,'http://66.media.tumblr.com/66f1f8fa7ef2baecf39a6086cde3e6cc/tumblr_n9a645JX891r2swomo2_r1_500.gif')
    if message.content == 'Pepsi':
        em = discord.Embed(description='Bebsi better')
        em.set_image(url='https://saudislike.files.wordpress.com/2009/05/pepsi.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '/Help':
        await client.send_message(message.channel,'The commands for this pile of shit are /Whogay, /Gay, /Coinflip, /Dice, /Bully, and /DIO. ')

client.run(os.getenv('TOKEN'))

