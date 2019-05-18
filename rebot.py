from wxpy import *
from tkinter import *

bot = Bot(cache_path=True)
tuling = Tuling(api_key='dcd4dba45c894ab098370a8b9936aa91')

@bot.register()
def auto_reply_all(msg):
    tuling.do_reply(msg)

embed()

