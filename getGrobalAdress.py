import credentials
import urllib.request
import discord

client = discord.Client()
# 起動時通知
@client.event
async def on_ready():
    print('Working')

#メッセージ分岐
@client.event
async def on_message(message):
    html =  urllib.request.urlopen('http://ipcheck.ieserver.net').read().decode('utf-8')
    if message.content.startswith('/gip'):
        await client.send_message(message.channel, html)

# bot起動
client.run(credentials.BOT_TOKEN)
