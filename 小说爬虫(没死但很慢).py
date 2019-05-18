import requests
import re
import os
from bs4 import BeautifulSoup
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_name1(url):
    name = {}
    response = requests.get(url,headers=header).text
    pat = 'div class="bookname">.*?target="_blank">(.*?)</a>'
    namels = re.compile(pat,re.S).findall(response)
    idls = re.compile('<a href="http://book.zongheng.com/book/(.*?).html" target="_blank">.*?</a>').findall(response)
    for i in range(len(namels)):
        name[namels[i]] = idls[i]
    for i in name:
        print(i)




def get_name(url):
    name = {}
    response = requests.get(url,headers=header).text
    pat = 'div class="bookname">.*?target="_blank">(.*?)</a>'
    namels = re.compile(pat,re.S).findall(response)
    idls = re.compile('<a href="http://book.zongheng.com/book/(.*?).html" target="_blank">.*?</a>').findall(response)
    for i in range(len(namels)):
        name[namels[i]] = idls[i]
    return name


#获得小说目录网址：
def get_story(s,name):
    if s in name:
        url = 'http://book.zongheng.com/showchapter/' + name[s] + '.html'
        return url
    else:
        print('不好意思没有这个小说')


def get_content(storyurl):
    contentls = []
    pat = '<a  href="(.*?)" target="_blank" title='
    time.sleep(10)
    url = requests.get(storyurl,headers=header).text
    response = re.compile(pat).findall(url)
    for link in response:
        time.sleep(10)
        r = requests.get(link,headers=header).text
        soup = BeautifulSoup(r,'lxml')
        content = soup.select('div[class="content"]')
        contentls.append(str(content))
    return contentls


def download(s):
    path = 'D:\爬虫\小说\\' + s
    E=os.path.exists(path)
    if not E:
        os.mkdir(path)
    ls = get_content(get_story(s,get_name(url)))
    k=0
    for i in range(len(ls)):
        k += 1
        f = open(path +'\\' + '第' + str(k) + '章' + '.txt','w',encoding='utf-8')
        content = ls[i].replace('</p>','\n').replace('<p>','').replace('[<div class="content" itemprop="acticleBody">','第{}章'.format(k)).replace('</div>]','')
        print('正在下载第{}章'.format(k))
        f.write(content)
        f.close()
    print('全部下载成功')


k = 0
for i in range(1,18): #设置页数
    url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p' + str(i) + '/v0/s1/t0/u0/i1/ALL.html'
    get_name1(url)
    print('------------------------------------------------------------------------','目录' + str(i))
    k += 1
n = input('有{}个目录请,请输入你想要的目录数：'.format(k))
url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p'+ n +'/v0/s1/t0/u0/i1/ALL.html'
s = input('请输入你要的书名：')
download(s)
