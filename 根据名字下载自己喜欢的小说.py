import requests
import re
from lxml import etree
import os


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_title(type,url):
    response = requests.get(url,headers=headers)
    response.encoding='gb2312' #不能忘记这个转码了
    response = response.text
    pat = '<li class="two"><a href="https://.*?" target="_blank">(.*?)全文阅读</a></li>'
    titles = re.compile(pat).findall(response)
    for i in range(len(titles)):
        print(titles[i]+'-----'+type[i])
    return titles

def love_page(id,url):
    response = requests.get(url,headers=headers)
    response.encoding='gb2312'
    response = response.text
    pat = '<li class="two"><a href="https://.*?" target="_blank">(.*?)全文阅读</a></li>'
    titles = re.compile(pat).findall(response)
    dict = {}
    for i in range(len(titles)):
        dict[titles[i]]=id[i]
    return dict

def get_type(url):
    response = requests.get(url,headers=headers)
    response.encoding='gb2312'
    response = response.text
    pat = '<li class="sev"><span><a href=".*?">(.*?)</a></span></li>'
    type = re.compile(pat).findall(response)
    return type

def get_id(url):
    response = requests.get(url,headers=headers)
    response.encoding='gb2312'
    response = response.text
    pat = '<li class="two"><a href="https://www.duquanben.com/xiaoshuo/(.*?)/" target="_blank">.*?</a></li>'
    id = re.compile(pat).findall(response)
    return id


def get_link(id):
    url = 'https://www.duquanben.com/xiaoshuo/' + id
    response = requests.get(url,headers=headers)
    response.encoding = 'gb2312'  # 不能忘记这个转码了
    response = response.text
    pat = '<li><a href="(.*?)">.*?</a></li>'
    linkls = re.compile(pat,re.S).findall(response)
    ls = []
    for i in linkls:
        newlink = url +'/'+ i
        ls.append(newlink)
    return ls


def main(name,links):
    path = 'D:\Study\爬虫\小说\\' + name
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
    n = 1
    for link in links:
        response = requests.get(link,headers=headers)
        response.encoding='gb2312'
        lxml = etree.HTML(response.text)
        content = lxml.xpath('//div[@id="htmlContent"]/text()')
        title = lxml.xpath("//title/text()")
        newtitle = ''.join(title)
        newcontent=''.join(content)
        newcontent = newcontent.replace('\xa0\xa0\xa0\xa0','\n')
        zhangjie = '第{}章'.format(n)
        f = open(path+'\\' + zhangjie + '.txt','w',encoding='utf-8')
        f.write(newtitle+'\n'+newcontent)
        print(zhangjie+'完成下载')
        n+=1
        f.close()


n = 1
for i in range(1,5): #这里调目录的页数
    url='https://www.duquanben.com/book/allvisit/0/' +str(i)+ '/'
    type = get_type(url)
    get_title(type,url)
    print('----------------------------------------------这是目录{}'.format(n))
    n += 1

if __name__=='__main__':
    s = input('请选择你喜欢的小说目录数：')
    name = input('请输入这目录你喜欢的小说：')
    url = 'https://www.duquanben.com/book/allvisit/0/' +s+ '/'
    id = get_id(url)
    love_page = love_page(id,url)
    for i in love_page:
        if name == i:
            links=get_link(love_page[i])
            main(name,links)
            break