# 💥 Killer Nuke Bot – Fastest Discord Nuker

**Killer Nuke Bot** is one of the fastest and most aggressive Discord nuker bots ever built — designed strictly for educational and controlled testing purposes. It performs rapid server destruction including mass banning, kicking, channel/role deletion, spam, and channel/role creation in seconds.

> ⚠️ **DISCLAIMER**  
> This tool is for **educational and testing** purposes **only**.  
> The author is **not responsible** for any damage, misuse, or abuse.  
> If you use this bot irresponsibly or violate Discord’s Terms of Service, it is entirely **your responsibility**.  
> Use only on Discord servers you **own** or have **explicit permission** to test on.

---

## 🚀 Features

| Command          | Description                                                      |
|------------------|------------------------------------------------------------------|
| `.help`          | Shows all available commands                                     |
| `.delchnls`.     | Deletes all channels in the server                               |
| `.delroles`      | Deletes all roles (excluding @everyone)                          |
| `.cchnls n name` | Creates `n` text channels using `name` as base                |
| `.crolee n name` | Creates `n` roles using `name` as base                        |
| `.spam n msg`.   | Sends `msg` in every channel `n` times                           |
| `.banall`        | Bans every member the bot can (excluding owner/self)             |
| `.kickall`       | Kicks every member the bot can (excluding owner/self)            |
| `.fuck`          | Full nuke: deletes all channels/roles, creates 30 of each, then spams

---

## ⚙️ Setup Instructions

### 1. Install dependencies

`pip install -U discord.py`

### 2. Configure your bot
Open `main.py` and replace:
bot.run("YOUR_BOT_TOKEN")
with your actual bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

### 3. Run the bot

`python killer.py`


Make sure your bot has **Administrator** permissions in the server.

---

## ☢️ Legal Notice

This bot executes mass-destructive actions and may violate Discord’s Terms of Service if misused. By using this software, you affirm that:

- You are using it **only** in environments where you are permitted.
- You understand the risk of getting your bot token **disabled** or **banned**.
- You accept full responsibility for your actions.

The developer of this Nuke Bot assumes **no liability** for abuse, server damage, or consequences that arise from the use of this code.

---

## 💻 Author

Developed by [`Killer`] — built for educational exploration and self-controlled testing only.



