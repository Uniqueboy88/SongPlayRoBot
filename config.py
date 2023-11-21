import os
API_ID = int(os.getenv("21140460"))
API_HASH = os.getenv("f235cdac2aa6454cc4755ab98970288a")
BOT_TOKEN = os.getenv("6784922632:AAF2m21bb5KV3DVEiIG_-Ao7TrJMVtRePKY")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
