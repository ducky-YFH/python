import json
import os
import random
from tkinter import *
from tkinter import messagebox

import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}
ls = []

def ensure():
    ls.clear()
    if text:
        text.delete(0,END)
    songer = entry.get()
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64653950969281607&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=' + songer + '&g_tk=5381&jsonpCallback=MusicJsonCallback5963715333145192&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
    response = requests.get(url, headers=headers).text
    response = response.replace('MusicJsonCallback5963715333145192(', '')
    response = response[0:-1]
    js = json.loads(response)
    list = js['data']['song']['list']
    # print(list)
    music = {}
    for i in list:
        mid = i['file']['media_mid']
        title = i['name']
        music[title] = mid
    for id in music:
        url1 = 'https://u.y.qq.com/cgi-bin/musicu.fcg? &g_tk=1796449428 &loginUin=508766975&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22songmid%22%3A%5B%22' + \
              music[id] + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%22508766975%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A508766975%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D'
        jsresponse = requests.get(url1, headers=headers).text
        js = json.loads(jsresponse)
        js2 = (js['req_0']['data']['midurlinfo'])
        music1 = {}
        for key in js2:
            vkey = key['purl']
            musiclink = 'http://musichy.tc.qq.com/amobile.music.tc.qq.com/' + vkey
            music1[id] = musiclink
            if music1 not in ls:
                ls.append(music1)
        for title in music1:
            text.insert(END,title)
            text.see(END)
            text.update()



def next_page():
    text.delete(0,END)
    songer = entry.get()
    global num
    num = random.choice([2,3,4,5])
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64653950969281607&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=' +str(num)+ '&n=20&w=' +songer+ '&g_tk=5381&jsonpCallback=MusicJsonCallback5963715333145192&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
    response = requests.get(url, headers=headers).text
    response = response.replace('MusicJsonCallback5963715333145192(', '')
    response = response[0:-1]
    js = json.loads(response)
    list = js['data']['song']['list']
    # print(list)
    music = {}
    for i in list:
        mid = i['file']['media_mid']
        title = i['name']
        music[title] = mid
    for id in music:
        url1 = 'https://u.y.qq.com/cgi-bin/musicu.fcg? &g_tk=1796449428 &loginUin=508766975&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22songmid%22%3A%5B%22' + \
              music[id] + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%22508766975%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A508766975%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D'
        jsresponse = requests.get(url1, headers=headers).text
        js = json.loads(jsresponse)
        js2 = (js['req_0']['data']['midurlinfo'])
        music1 = {}
        for key in js2:
            vkey = key['purl']
            musiclink = 'http://musichy.tc.qq.com/amobile.music.tc.qq.com/' + vkey
            music1[id] = musiclink
            if music1 not in ls:
                ls.append(music1)
        for title in music1:
            text.insert(END,title)
            text.see(END)
            text.update()


def download():
    path = 'D:/音乐'
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    for music in ls:
        for MS in music:
            love = entry1.get()
            if love == MS:
                f = open(path + '\\' + love + '.mp3', 'wb')
                last = requests.get(music[MS], headers).content
                f.write(last)
                f.close()
                text1.insert(END, '{}:下载成功'.format(love))
                text1.see(END)
                text1.update()

def look():
    messagebox.showinfo('文件路径','D:\音乐')


root = Tk()
root.title('qq音乐下载器')
root.geometry('670x450+450+200')

label = Label(root,text='请输入你要的歌曲名或者是歌手名：',font=('微软雅黑',15))
label.grid(row=0,column=0)
entry = Entry(root,font=('宋体',15))
entry.grid(row=0,column=1)

label1 = Label(root,text='从上面的列表选择你想下载的音乐：',font=('微软雅黑',15))
label1.grid(row=2,column=0)
entry1 = Entry(root,font=('宋体',15))
entry1.grid(row=2,column=1)


text = Listbox(root,font=('宋体',12),width=40,height=20,bg='pink')
text.grid(row=1,column=0)


text1 = Listbox(root,font=('宋体',12),width=40,height=20,bg='pink')
text1.grid(row=1,column=1)


button = Button(root,text='下一页',font=('微软雅黑',10),command=lambda:next_page())
button.grid(row=3,column=0,sticky='W')

button1 = Button(root,text='点击下载',font=('微软雅黑',10),command=lambda :download())
button1.grid(row=2,column=1,sticky='E')


button2 = Button(root,text='确定',font=('微软雅黑','10'),command=lambda:ensure())
button2.grid(row=0,column=1,sticky='E')

button3 = Button(root,text='查看下载路径',font=('微软雅黑','10'),command=look)
button3.grid(row=3,column=1)


root.mainloop()
