import os
import dotenv

dotenv.load_dotenv('.env')

API_KEY = os.environ['API_KEY']
DB_PASSWORD = os.environ['DB_PASSWORD']
TOKEN_BOT = os.environ['TOKEN_BOT']
API_URL = os.environ['API_URL']

