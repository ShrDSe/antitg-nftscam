import os
from dotenv import load_dotenv

load_dotenv() 

API_ID = os.getenv('API_ID')
API_HASH = str(os.getenv('API_HASH'))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))