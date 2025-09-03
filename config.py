#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "24894984"))
    API_HASH = os.environ.get("API_HASH", "4956e23833905463efb588eb806f9804")
    AUTH_USERS = "7693352537"


