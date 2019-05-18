import requests
import time
import re
import urllib.request

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400"}

#获得1-4页的网页：
def get_url():
    urlList=[]
    for i in range(1,5):
        html='http://www.win4000.com/zt/qiche_'+str(i)+'.html'
        urlList.append(html)
    return urlList

#获得每页的压缩图片链接
def get_picture_link(urls):
    lk=[]
    pat_link = 'data-original = "(.*?)" />'
    for url in urls:
        url = requests.get(url,headers=headers).text
        link = re.compile(pat_link).findall(url)
        for i in link:
            lk.append(i)
    return lk

#获得每页的压缩图片名字
def get_pic(urls):
    ls=[]
    pat_name = 'title="(.*?)" target="_blank"'
    for url in urls:
        url = requests.get(url, headers=headers).text
        name = re.compile(pat_name).findall(url)
        for i in name:
            ls.append(i)
    return ls


def down_pic(urllink,n):
    for i in range(len(n)):
        path = 'D:\下载\\' + n[i] + '.jpg'
        contet = requests.get(urllink[i])
        contet = contet.content
        f=open(path,'wb')
        f.write(contet)
        f.close()

down_pic(get_picture_link(get_url()),get_pic(get_url()))