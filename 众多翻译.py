import requests
import json
from tkinter import *


def CH_JP(event):
    text.delete(1.0,END)
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}
    url = 'http://cn.bing.com/ttranslate?&category=&IG=D0B5D42530A8410B9D4DCB0E55BABE28&IID=translator.5036.1'
    content = entry.get()
    data = {
        'from':'zh-CHS',
        'to':'ja',
        'text': content
    }
    response = requests.post(url,headers=header,data=data).text
    js = json.loads(response)
    last = js['translationResponse']
    text.insert(1.0,last)



root = Tk()
root.title('Translator')
root.geometry('352x256+600+200')
label_one = Label(root, font=('微软雅黑', 12), text='中翻日：')
label_one.grid(row=0, column=0)

text = Text(root, font=('微软雅黑', 12), fg='purple', width='38', height='10')
text.grid(row=2, columnspan=3)

entry = Entry(root, font=('微软雅黑', 12), width='30', foreground='purple')
entry.grid(row=0, column=1)
entry.bind('<Return>', CH_JP)



root.mainloop()
