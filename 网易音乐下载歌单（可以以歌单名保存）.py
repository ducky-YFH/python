import requests
from bs4 import BeautifulSoup
import os
from tkinter import *


def start():
    text.delete(0,END)
    url = entry.get()
    url = url.replace('#/','')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2565.400'}
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    title = str(soup.title).replace('<title>', '').replace('</title>', '')
    path = 'D:/音乐'+'/'+title
    if not os.path.exists(path):
        os.mkdir(path)
    dict = {}
    for i in soup.ul:
        i = str(i)
        pat = 'id=(.*?)">(.*?)</a>'
        songs = re.compile(pat).findall(i)
        songs=songs[0]
        dict[songs[1]] = songs[0]
    for name in dict:
        url = 'http://music.163.com/song/media/outer/url?id=' + dict[name] + '.mp3'
        music = requests.get(url,headers=headers).content
        f = open(path+'//'+name+'.mp3','wb')
        f.write(music)
        f.close()
        text.insert(END,name+'---下载成功')
        text.see(END)
        text.update()
    text.insert(END,'一共{}首'.format(len(dict)))


root = Tk()
root.title('网易音乐歌单下载器')
root.geometry('460x490+450+250')

label = Label(root,text='请放入你喜欢的歌单：',font=('微软雅黑',12))
label.grid(row=0,column=0)

entry = Entry(root,font=('微软雅黑',12),fg='green')
entry.grid(row=0,column=1,sticky='E')

text = Listbox(root,font=('微软雅黑',12),fg='green',width=50,height=20)
text.grid(row=1,columnspan=3)

button = Button(root,text='确定',font=('微软雅黑',10),command=start)
button.grid(row=0,column=2,sticky='E')


root.mainloop()

