import discord, os, random
from discord.ext import commands
from bot_logic import sampah_anorganik, sampah_organik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def shh(ctx, count_shh = 3):
    await ctx.send("shh" * count_shh)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def anorganik(ctx):
    await ctx.send(sampah_anorganik())

@bot.command()
async def organik(ctx):
    await ctx.send(sampah_organik())

bot.run("Taruh token kamu disini!")
