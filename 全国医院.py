import requests
import re
from lxml import etree
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400"}

def get_province(url):
    response = requests.get(url,headers=headers).text
    pat = 'a href=".*?" target="_blank" title="(.*?)" class="aere-txt2">.*?</a>'
    province = re.compile(pat).findall(response)
    return province



def get_all(url):
    response = requests.get(url, headers=headers).text
    pat = 'a href="/(.*?)/" target="_blank" title=".*?" class="aere-txt2">.*?</a>'
    all = re.compile(pat).findall(response)
    return all

def get_allurl(url):
    all = get_all(url)
    ls = []
    for i in all:
        url = 'https://yyk.99.com.cn/' +i+ '/'
        ls.append(url)
    return ls


def get_shiqu(f,allurl):
    response = requests.get(allurl,headers=headers).text
    lxml = etree.HTML(response)
    counts = lxml.xpath('//div[@class="m-box"]/h3')
    for count in counts:
        hoscount = count.xpath('..//span/text()')
        hosname = count.xpath('..//td/a/@title')
        hosid = count.xpath('..//td/a/@href')
        GG = (''.join(hoscount))
        print(GG)
        f.write(GG+'\n'+'-------------------------------'+'\n')
        for i in range(len(hosid)):
            try:
                url = 'https://yyk.99.com.cn' + hosid[i]
                content = requests.get(url,headers=headers).text
                pinfen = re.compile('<li><span>(.*?)</span><script>showScore(.*?)</script></li>').findall(content)
                jianjie = re.compile('<div class="hospital-info">.*?<p>(.*?)<a',re.S).findall(content)
                phone = re.compile('<p><span>电话：</span><em>(.*?)</em>').findall(content)
                PF = (''.join(pinfen[0])+''.join(pinfen[1])+''.join(pinfen[2]))
                JJ = (''.join(jianjie))
                PH =(''.join(phone))
                f.write('医院名称：'+hosname[i]+'\n'+'电话号码：' +PH+ '\n'+'简       介：'+'\n'+JJ+'\n'+'医院评分：'+'\n'+PF+'\n'+'\n'+'-----------------------------------------------------'+'\n')
                print('下载{}资料成功'.format(hosname[i]))
            except:
                pass
    print('--------------------------------------------------------------------------------------------------------------')



def main():
    url = 'https://yyk.99.com.cn/'
    province=get_province(url)
    path = 'D:/爬虫/医院'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    PROurl = get_allurl(url)
    for i in range(len(PROurl)):
        f = open(path + '\\' + province[i] + '.txt', 'a+', encoding='utf-8')
        get_shiqu(f,PROurl[i])
        f.close()


if __name__== '__main__':
    main()