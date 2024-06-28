import discord
import services


DISCORD_TOKEN = "MTI1NTcyMTI1MDIyNDA4MzAxNg.GccmvS.-1Ug5P3O7WR5BlJuLBCmq_H84lSRdTfPJAScbE"
CMD_CHAT = "!chat"
CMD_IMAGE = "!image"
CMD_CAPTION = "!caption"

intents = discord.Intents.default()
intents.message_content = True 

bot = discord.Client(intents=intents)

# HOC / HOF /Annotation / Decorator (High Order Coponents, High Order Function)
@bot.event 
async def on_ready():
    print(f"We have logged in as {bot.user}")

# if-cause
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if message.content.startswith(CMD_CHAT):
        prompt = message.content.replace(CMD_CHAT, "").strip()
        response = services.use_gpt(prompt)
        await message.channel.send(response)  # await ใช้ได้แค่กับ await function

    if message.content.startswith(CMD_IMAGE):
        prompt = message.content.replace(CMD_IMAGE, "").strip()
        file = services.use_stable_diffusion(prompt)
        await message.channel.send(file=file)
    
    if message.content.startswith(CMD_CAPTION) and len(message.attachments) > 0:
        caption = services.use_dall_e(message.attachments[0].url)
        await message.channel.send(caption) 

bot.run(DISCORD_TOKEN) 