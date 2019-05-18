import requests
import re
import os
from threading import Thread
from lxml import etree

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_story(url):
    response = requests.get(url,headers=headers).text
    html = etree.HTML(response)
    top = html.xpath('//div[@class="info fl"]')
    storyDict = {}
    for i in top:
        title = i.xpath('.//h3/a/text()')[0]
        autor = i.xpath('.//div/text()')[0]
        introduce = i.xpath('.//div/text()')[1]
        storyDict[title] = autor +'\n'+ introduce +'\n'
        print(title+'\n'+storyDict[title]+'\n')
    print('---------------------------------------')



for i in range(1,2000):
    url = 'https://xiaoshuo.sogou.com/1_0_0_0_heat/?pageNo='+str(i)
    th = Thread(target=get_story,args=(url,))
    th.start()
