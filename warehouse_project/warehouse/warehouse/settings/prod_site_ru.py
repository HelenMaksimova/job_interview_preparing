from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

SITE_ID = 2

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
