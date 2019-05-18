import requests
import os
import re
from threading import Thread


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400"}
n = 1

def getPicUrl(url):
    response = requests.get(url, headers=headers).text
    pat = '<li><a href="/desk/(.*?).htm" title="'
    idls = re.compile(pat).findall(response)
    for i in idls:
        picUrl = 'http://www.netbian.com/desk/' + i + '-1920x1080.htm'
        response = requests.get(picUrl, headers=headers).text
        pat = '<a href="http://img.netbian.com/(.*?)" title='
        GaoQing = re.compile(pat).findall(response)
        kk = ''.join(GaoQing)
        bizhiUrl = ('http://img.netbian.com/' + kk)
        th = Thread(target=download,args=(bizhiUrl,))
        th.start()


def download(bizhiUrl):
    global n
    path = 'D:/爬虫/利用多线程下载的高清壁纸2'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    pic = requests.get(bizhiUrl,headers=headers).content
    f = open(path +'\\'+ str(n) +'.jpg','wb')
    n += 1
    f.write(pic)
    print('下载第{}张成功'.format(n))

def main():
    for i in range(229,1240):
        url = 'http://www.netbian.com/index_' +str(i)+ '.htm'
        getPicUrl(url)


if __name__ == '__main__':
    main()
