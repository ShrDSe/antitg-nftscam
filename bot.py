import re, requests
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client('anti_shit', 
            api_id=API_ID, 
            api_hash=API_HASH, 
            bot_token=BOT_TOKEN)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


@bot.on_message(filters.text)
async def check_link(client, message):
    links = re.findall(r'(https?://\S+)', message.text)
    if links:
        print(links)
        for link in links:
            if requests.get(link + 'images/hero.png', headers=headers).status_code == 200:
                await message.delete()
                print("deleted " + link)
                break

bot.run()
