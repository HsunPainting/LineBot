# 塔羅牌

from linebot import LineBotApi
from linebot.models import *

import os
import json
import random
from apps.common.common import *

from apps.ai.gemini import gemini

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
print('Hi, 你好!')


