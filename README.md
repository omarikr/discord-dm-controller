# Discord Bot: Interactive DM Controller

This Python 3 script starts a Discord bot that opens a direct message (DM) session with a specified controller user as soon as the bot is online. You can send messages to the user directly from the terminal, and receive and display their replies live.

## 📌 Features

- Automatically opens a DM with a specific user on startup
- Sends an initial welcome message
- Terminal input for sending DMs
- Live logging of incoming messages from the controller user
- Clean and minimal interface for live chatting

## 🚀 How It Works

1. The bot connects to Discord and DMs the specified user (`controller_user_id`).
2. You can send messages from the terminal.
3. When the controller replies, messages are displayed live.
4. Type new messages at any time by pressing `Enter`.

## 🛠️ Requirements

- Python 3.7+
- `discord.py` library

## 🛠️ Setup

1. Clone this repository:

```
git clone https://github.com/yourusername/discord-dm-controller.git
cd discord-dm-controller
```
2. Edit the script and replace:
```
TOKEN = "YOUR_BOT_TOKEN"
CONTROLLER_ID = 1066707409206267914
```
3. Install dependencies
```
   pip install -U discord.py
```
4. Run the bot
```
python3 bot.py
```
