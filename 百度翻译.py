import requests
import json
from tkinter import *


def Chinese_English(event):
    text.delete(0,END)
    name = entry.get()
    try:
        url = 'https://fanyi.baidu.com/multitransapi'
        data = {
            'from':'zh',
            'query':name,
            'simple_means_flag':'3',
            'to':'en',
            }
        response = requests.post(url, data=data).text
        js = json.loads(response)
        ls = js['data']['cands']
        for i in ls:
            text.insert(END,i)
    except:
        wrong = '没反应再按一次!!!'
        text.insert(END,wrong)


def English_Chinese(event):
    text.delete(0,END)
    name2 = entry2.get()
    try:
        url = 'https://fanyi.baidu.com/multitransapi'
        data2 = {
            'from': 'en',
            'query': name2,
            'simple_means_flag': '3',
            'to': 'zh',
        }
        response = requests.post(url, data=data2).text
        js = json.loads(response)
        ls = js['data']['cands']
        for i in ls:
            text.insert(END,i)
    except:
        wrong = '没反应再按一次!!!'
        text.insert(END, wrong)




root = Tk()
root.title('翻译器')
root.geometry('480x400+460+260')
label = Label(root,text=('中翻英：'),font=('微软雅黑',12))
label.grid(row=0,column=0)

label2 = Label(root,text=('英翻中：'),font=('微软雅黑',12))
label2.grid(row=1,column=0)

entry = Entry(root,font=('微软雅黑',12),foreground = 'green')
entry.grid(row=0,column=1)
entry.bind('<Return>',Chinese_English)

entry2 = Entry(root,font=('微软雅黑',12),foreground = 'green')
entry2.grid(row=1,column=1)
entry2.bind('<Return>',English_Chinese)

text = Listbox(root,font=('微软雅黑',12),height=15,width=52,foreground = 'green')
text.grid(columnspan=5)

root.mainloop()
