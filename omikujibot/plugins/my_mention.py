from slackbot.bot import respond_to
import random

@respond_to("ひく")
def omikuji(a):
    a.reply(random.choice(["大吉です！🎉", "吉です！！🎉", "中吉です！！", "小吉
です！！", "半吉です！！", "末吉です！！", "末小吉です！！"]))
