import discord
from discord.ext.commands import Bot
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#^Not all of these are used. I just copied all of it from my bot.
#Install Pillow if not already.

BOT_PREFIX = ("~", ">")  #Change the prefix to whatever you want
TOKEN = "Your Token Goes Here"
client = Bot(command_prefix=BOT_PREFIX) #sets the command prefix


@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Make sure you insert a valid font from your folder.
    fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
    draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig) #draws Information
    draw.text((50, 500), "Username: {}".format(user.name), (255, 255, 255), font=font) #draws the Username of the user
    draw.text((50, 700), "ID:  {}".format(user.id), (255, 255, 255), font=font) #draws the user ID
    draw.text((50, 900), "User Status:{}".format(user.status), (255, 255, 255), font=font) #draws the user status
    draw.text((50, 1100), "Account created: {}".format(user.created_at), (255, 255, 255), font=font) #When the account was created 
    draw.text((50, 1300), "Nickname:{}".format(user.display_name), (255, 255, 255), font=font) # Nickname of the user
    draw.text((50, 1500), "Users' Top Role:{}".format(user.top_role), (255, 255, 255), font=font) #draws the top rome
    draw.text((50, 1700), "User Joined:{}".format(user.joined_at), (255, 255, 255), font=font) #draws info about when the user joined
    img.save('infoimg2.png') #Change infoimg2.png if needed.
    await client.upload("infoimg2.png")
    
    
client.run(TOKEN)
    
 
