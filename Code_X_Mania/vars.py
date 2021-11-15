# (c) Code-x-Mania

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '7523379'))
    API_HASH = str(getenv('API_HASH', 'ce43762f206dc2a2eb115986fbe3b4a2'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '2114312285:AAF1Mzn30tfFi69RgcIPp377JIQE05jIbv0'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001523128336'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '429535048'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'MrAnonymousX'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'tiny.one/rlystream')) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "{}".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://zoredeaxx:<zoredeaxx>@cluster0.uemqk.mongodb.net/zorstream?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
