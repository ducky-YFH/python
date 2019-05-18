import threading
import requests
import os
from bs4 import BeautifulSoup
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}

def Get_music(url):
    url = url.replace('#/','')
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,'lxml')
    dict = {}
    ls = []
    for i in soup.ul:
        i = str(i)
        pat = 'id=(.*?)">(.*?)</a>'
        songs = re.compile(pat).findall(i)
        songs=songs[0]
        dict[songs[1]] = songs[0]
    for name in dict:
        ls.append('http://music.163.com/song/media/outer/url?id=' + dict[name] + '.mp3')
    TH(ls)

x = 0

def download(urls):
    path = 'D:/音乐/网易'
    global x
    if not os.path.exists(path):
        os.mkdir(path)
    music = requests.get(urls, headers=headers).content
    f = open(path + '//' + str(x) + '.mp3', 'wb')
    x += 1
    f.write(music)
    f.close()
    print(str(x) + '---下载成功')



def TH(ls):
    for i in ls:
        th = threading.Thread(target=download,args=(i,))
        th.start()


def main():
    url = 'https://music.163.com/#/playlist?id=2299414191'
    Get_music(url)



if __name__ == '__main__':
    main()