import requests
import re
import time
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400"}


def get_ID(url):
    pat = '<li><a href="/desk/(.*?).htm"'
    url = requests.get(url,headers=headers).text
    IDlist = re.compile(pat).findall(url)
    return IDlist

#获得第一页的网址
def get_firsturl():
    url = 'http://www.netbian.com/fengjing/index.htm'
    return url


#或的2-5的网址
def get_url(i):
    url = 'http://www.netbian.com/fengjing/index_'+str(i)+'.htm'
    return url


def get_name(url):
    pat = 'title="(.*?)" target="_blank"><img'
    ul = requests.get(url,headers=headers).text
    namels = re.compile(pat).findall(ul)
    return namels

#构建高清图片网址：
def get_pic(IDList):
    ls = []
    for Id in IDList:
        picurl= 'http://www.netbian.com/desk/'+Id+'-1920x1080.htm'
        ls.append(picurl)
    return ls

#获得最终高清的地址：
def get_piclink(urlls):
    pat = '<a href="http://img.netbian.com/(.*?).jpg" title="'
    ls = []
    for url in urlls:
        link = requests.get(url).text
        ID = re.compile(pat).findall(link)
        s=''
        for i in ID:
            s+=i
        lasturl = 'http://img.netbian.com/'+s+'.jpg'
        ls.append(lasturl)
    return ls

def download(namels,linkls):
    s=0
    for i in range(len(namels)):
        path = 'D:\爬虫\爬虫图片\\' + namels[i] + '.jpg'
        link = linkls[i]
        f=open(path,'wb')
        content = requests.get(linkls[i]).content
        f.write(content)
        s+=1
        time.sleep(1)
        print('现在爬到第'+str(s)+'个')



for i in range(2,10):
    print('正在开始爬第{}页-------------------------------------'.format(i))
    download(get_name(get_url(i)),get_piclink(get_pic(get_ID(get_url(i)))))
