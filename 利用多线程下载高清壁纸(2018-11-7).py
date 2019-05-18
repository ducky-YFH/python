import requests
import os
import re
from lxml import etree
from threading import Thread

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}
n = 1

def get_ID(url):
    response = requests.get(url,headers=headers).text
    pat = '<a href="(.*?)" alt="?'
    links = re.compile(pat).findall(response)
    return links

def get_pic(links):
    urls = []
    for url in links:
        response = requests.get(url,headers).text
        html = etree.HTML(response)
        at_lasts = html.xpath('//div[@class="scroll-img-cont"]/ul/li/a/img/@data-original')
        urls.append(at_lasts)
    return urls

def TH(urls):
    for i in urls:
        for j in i:
            pic_link = j.replace('_120_80', '')
            th = Thread(target=download,args=(pic_link,))
            th.start()

def download(pic_link):
    global n
    path = 'D:/爬虫/美桌网的壁纸'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    pic = requests.get(pic_link,headers=headers).content
    f = open(path+'//'+str(n)+'.jpg','wb')
    f.write(pic)
    print('下载第{}张成功'.format(n))
    n += 1


def main():
    for i in range(5):
        url = 'http://www.win4000.com/wallpaper_0_0_10_' +str(i)+ '.html'
        links = get_ID(url)
        urls = get_pic(links)
        TH(urls)

if __name__ == '__main__':
    main()