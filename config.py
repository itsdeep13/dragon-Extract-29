#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8034429795:AAGzFsK8gIuz02AMUAtNsA0AcTYFdk2Kr5Q")
    API_ID = int(os.environ.get("API_ID", "27473563"))
    API_HASH = os.environ.get("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
    AUTH_USERS = "6363345131"



