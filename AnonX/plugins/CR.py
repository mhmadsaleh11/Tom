import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒محمد صالحَّّ ", url=f"https://t.me/R_9_9_0"), 
                 ],[
                    InlineKeyboardButton(
                        "محمد صالح", url=f"https://t.me/R_9_9_0"),
                ],[
                    InlineKeyboardButton(
                        "𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂", url=f"https://t.me/CCA6A"),
                    InlineKeyboardButton(
                        "محمد صالح", url=f"https://t.me/R_9_9_0"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝⚡", url=f"https://t.me/CCA6A"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["توم انجم","احمد","توم","مبرمج","TOM","tom"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("R_9_9_0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين انجم","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("R_9_9_0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كريستين انجم","كريستين","كرستين","الدكتوره","cristin","كرستينه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("CCA6A")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مانو انجم","مانو","الممول","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("R_9_9_0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒محمد صالحَّّ", url=f"https://t.me/R_9_9_0"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝⚡", url=f"https://t.me/CCA6A"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒محمد صالحَّّ", url=f"https://t.me/R_9_9_0"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐖𝐀𝐓𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 ⌝⚡", url=f"https://t.me/CCA6A"),
                ],

            ]

        ),

    )



    
