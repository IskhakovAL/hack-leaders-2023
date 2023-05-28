from os import getenv

from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_DB = getenv('POSTGRES_DB')
POSTGRES_PORT = getenv('POSTGRES_PORT')
HOSTNAME = getenv('HOSTNAME')
YANDEX_API_KEY = getenv('YANDEX_API_KEY')

SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = "HS256"
