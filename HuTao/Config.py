#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6653243642:AAEaI93MNElP8WXsQ59AZWZgvnZ1WpnVTyY"
    API_ID =  24427150# API ID
    API_HASH = "9fcc60263a946ef550d11406667404fa" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "NovaSupports" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001816188874 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("6149191605").split()}) #OWNER ID

DB_URL = "mongodb+srv://shekharhatture:kUi2wj2wKxyUbbG1@cluster0.od4v7eo.mongodb.net/?retryWrites=true&w=majority" # MONGO DB URL

SQL_URL = "postgres://dfoicjez:fn9pjJgBY6x0rfTme5f37MRKmClTjo4p@silly.db.elephantsql.com/dfoicjez" # ELEPHANT SQL URL
