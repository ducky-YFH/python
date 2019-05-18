import requests
import json
from tkinter import *


def CH_EN(event):
        try:
            text.delete(1.0,END)
            text2.delete(1.0,END)
            url = 'http://cn.bing.com/ttranslate?&category=&IG=D0B5D42530A8410B9D4DCB0E55BABE28&IID=translator.5036.1'
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}
            name = entry.get()
            data = {
                    'text': name,
                    'from':'zh-CHS',
                    'to':'en'
                    }
            response = requests.post(url,data=data,headers=headers).text
            js = json.loads(response)
            text.insert(END,js['translationResponse'])
            text2.insert(END,name)
        except:
            text.insert(END,'没反应请再按一次')


def EN_CH(event):
        try:
            text.delete(1.0, END)
            text2.delete(1.0,END)
            url = 'http://cn.bing.com/ttranslate?&category=&IG=D0B5D42530A8410B9D4DCB0E55BABE28&IID=translator.5036.1'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}
            name2 = entry2.get()
            data = {
                    'text': name2,
                    'from':'en',
                    'to':'zh-CHS'
                    }
            response2 = requests.post(url,data=data,headers=headers).text
            js2 = json.loads(response2)
            text.insert(END,js2['translationResponse'])
            text2.insert(END, name2)
        except:
            text.insert(END,'没反应再按一次')




root = Tk()
root.title('微软翻译器')
root.geometry('480x700+460+260')
label = Label(root,text=('中翻英：'),font=('微软雅黑',12))
label.grid(row=0,column=0)

label2 = Label(root,text=('英翻中：'),font=('微软雅黑',12))
label2.grid(row=1,column=0)

label3 = Label(root,text=('提示：'),font=('微软雅黑',12),fg='red')
label3.grid(row=0,column=2,sticky='')

label4 = Label(root,text=('按回车确定'),font=('微软雅黑',12))
label4.grid(row=1,column=2,sticky='E')


entry = Entry(root,font=('微软雅黑',12),foreground = 'green')
entry.grid(row=0,column=1)
entry.bind('<Return>',CH_EN)

entry2 = Entry(root,font=('微软雅黑',12),foreground = 'green')
entry2.grid(row=1,column=1)
entry2.bind('<Return>',EN_CH)

text = Text(root,font=('微软雅黑',12),height=15,width=52,foreground = 'green')
text.grid(columnspan=5)

text2 = Text(root,font=('微软雅黑',12),height=15,width=52,foreground = 'purple')
text2.grid(row=3,columnspan=5)

root.mainloop()
