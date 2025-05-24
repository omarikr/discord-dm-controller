import discord
import asyncio
import threading

TOKEN = "YOUR_BOT_TOKEN"
CONTROLLER_ID = 1066707409206267914

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True

client = discord.Client(intents=intents)
controller_user = None
controller_dm = None

def input_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        msg = input("Enter message to send: ")
        if msg.strip() == "":
            continue
        coro = controller_dm.send(msg)
        future = asyncio.run_coroutine_threadsafe(coro, client.loop)
        try:
            future.result()
            print("DMed the content, wait for a response or press enter to send a new message")
        except Exception as e:
            print(f"Error sending DM: {e}")

@client.event
async def on_ready():
    global controller_user, controller_dm
    controller_user = await client.fetch_user(CONTROLLER_ID)
    controller_dm = await controller_user.create_dm()
    await controller_dm.send("📌 Your session has been started with controller of this bot, you'll be chatting lively with he/she now!")
    print(f"Bot is ready and connected to {controller_user.name}.")
    threading.Thread(target=input_loop, daemon=True).start()

@client.event
async def on_message(message):
    if message.author.id == CONTROLLER_ID and isinstance(message.channel, discord.DMChannel):
        print(f"\nDM Received: {message.content}")
        print("Press enter to send your DM")

client.run(TOKEN)
