from os import getenv

API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6329875412").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/5946d56c70ac0ced52b18.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/TeamEspro/EsproUserBot")
BRANCH = getenv("BRANCH", "ritik")
