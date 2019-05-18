import re
import requests
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400"}

def get_GaoQing(url):
    response = requests.get(url,headers=headers).text
    pat = '<li><a href="/desk/(.*?).htm" title="'
    idls = re.compile(pat).findall(response)
    ls = []
    for i in idls:
        url = 'http://www.netbian.com/desk/' +i+ '-1920x1080.htm'
        ls.append(url)
    return ls


def main(n,ls):
    path = 'D:/爬虫/终极高清图片'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    for url in ls:
        f = open(path + '//' + str(n) + '.jpg','wb')
        response = requests.get(url,headers=headers).text
        pat = '<a href="http://img.netbian.com/(.*?)" title='
        GaoQing = re.compile(pat).findall(response)
        kk=''.join(GaoQing)
        bizhi=('http://img.netbian.com/'+kk)
        GG=requests.get(bizhi,headers=headers).content
        f.write(GG)
        n += 1
        print('现在下载到第{}张'.format(n))
    return n



if __name__=="__main__":
    n = 1
    for i in range(2,100):
        url = 'http://www.netbian.com/index_' + str(i) + '.htm'
        k = main(n,get_GaoQing(url))
        n = 0
        n += k


