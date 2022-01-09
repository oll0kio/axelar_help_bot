import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))
admin_id = str(os.getenv("ADMIN_ID"))

# DB settings
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


lp_token = os.getenv("LIQPAY_TOKEN")