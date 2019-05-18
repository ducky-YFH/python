import requests
import re
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

#获取小说ID列表
def get_ID(url):
    content = requests.get(url,headers=header).content
    soup = BeautifulSoup(content,'lxml')
    pat = str(soup.select('a'))
    pat2 = '<a href="http://www.17k.com/book/(.*?).html"'
    contentList = re.compile(pat2).findall(pat)
    return contentList

#获取小说网址,返回小说网址列表
def get_story(IDlist):
    ls=[]
    for ID in IDlist:
        url = 'http://www.17k.com/list/' +ID+ '.html'
        ls.append(url)
    return ls

#获取小说名字,返回名字列表
def get_name(urlls):
    pat = '<title>(.*?)</title>'
    namels=[]
    for url in urlls:
        s=''
        response = requests.get(url,headers=header)
        response.encoding = 'utf-8'
        last = response.text
        name = re.compile(pat).findall(last)
        for i in name:
            s+=i
        namels.append(s)
    return namels


#获取每个小说里面的章节列表：
def get_storylist(urlls):
    pat = 'href="(.*?)" title="字数'
    n=0
    ls2=[]
    for url in urlls:
        ls=[]
        response = requests.get(url,headers=header)
        response.encoding = 'utf-8'
        url2=response.text
        link = re.compile(pat).findall(url2)
        for i in link:
            s = 'http://www.17k.com/' + i
            ls.append(s)
        ls2.append(ls)
        n+=1
    return ls2

def down_everystroy(storylist,namels):
    path = 'D:\爬虫\爬虫小说\\'
    n=0
    for ls in storylist:
        f=open(path + namels[n] + '.txt','w')
        n+=1
        s=''
        for link in ls:
            s+=link+'\n'
        f.write(s)
        print('第{}个小说的网址爬取成功'.format(n))
        f.close()




url = 'http://www.17k.com/mianfei/'
down_everystroy(get_storylist(get_story(get_ID(url))),get_name(get_story(get_ID(url))))
