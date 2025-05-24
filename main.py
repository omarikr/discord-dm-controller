# <---------------------------- © 2025 - Developed by omarikr All rights reserved ---------------------------->

import discord
import asyncio
import threading

TOKEN = "YOUR_BOT_TOKEN" # <------- Input your discord bot token which you want to send DMs with.
CONTROLLER_ID = 1066707409206267914 # <------- Input the ID of the account you want the bot send and receive DMs from 

# <--------------- Basic required intents which should be enabled from discord developer portal --------------->

intents = discord.Intents.default() 
intents.messages = True
intents.dm_messages = True

# <--------------- Bot setup--------------->

client = discord.Client(intents=intents) #
controller_user = None
controller_dm = None

# <--------------- Main DM Controller script--------------->

def input_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        msg = input("Enter message to send: ")
        if not msg.strip():
            continue
        future = asyncio.run_coroutine_threadsafe(controller_dm.send(msg), client.loop)
        try:
            future.result()
            print("DMed the content, wait for a response or press enter to send a new message")
        except Exception as e:
            print(f"Error sending DM: {e}")

# <--------------- On ready event, DMs the controller ID make sure controller's DMs are enabled --------------->

@client.event
async def on_ready():
    global controller_dm
    controller_user = await client.fetch_user(CONTROLLER_ID)
    controller_dm = await controller_user.create_dm()
    await controller_dm.send("📌 Your session has been started with controller of this bot, you'll be chatting lively with he/she now!")
    await client.change_presence(status=discord.Status.dnd, activity=discord.CustomActivity(name=f"Chatting with {controller_user.name}!"))
    print(f"Bot is ready and connected to {controller_user.name}.")
    threading.Thread(target=input_loop, daemon=True).start()

# <--------------- Received message logging and next message option --------------->

@client.event
async def on_message(message):
    if message.author.id == CONTROLLER_ID and isinstance(message.channel, discord.DMChannel):
        print(f"\nDM Received: {message.content}")
        print("Press enter to send your DM")

# <--------------- Finishing line so the bot successfully starts  --------------->

client.run(TOKEN)
print("💖 Thanks for using my script, Support me by donating LTC at ltc1qwcsuxzuezcs8m2r8zvdaphl93ym3juy9cmlt9x and joining my discord server https://discord.gg/bxQnmFn7eU")
print("💼 To donate and support me: ltc1qwcsuxzuezcs8m2r8zvdaphl93ym3juy9cmlt9x")
print("🚀 Have questions? Need support? Or do you need a free hosting for it! Join us at https://discord.gg/eUyr8T5JYm")
