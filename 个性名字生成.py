import requests
from tkinter import *
from lxml import etree
import time

def start():
    word = input('请输入你的名字：')
    data = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'m.kachayv.cn',
        'Origin':'http://m.kachayv.cn',
        'Referer':'http://m.kachayv.cn/',
        'Upgrade-Insecure-Requests':'1',
        'word': word,
        'fonts':'8.ttf',
        'sizes':'60',
        'fontcolor':'#ffffff',
        'colors':'#FD5668'
        }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}
    url = 'http://m.kachayv.cn/'
    time1 = time.time()
    response = requests.post(url, data=data, headers=headers)
    time2 = time.time()
    print(time2-time1)
    response.encoding = 'utf-8'
    response = response.text
    lxml = etree.HTML(response)
    # name = lxml.xpath('//textarea/text()')[0]
    id = lxml.xpath('//div[@class="sctp"]/img/@src')[0]
    id = id.replace('cache/', '').replace('.png', '')
    signatureUrl = 'http://m.kachayv.cn/cache/' + id + '.png'
    # signature = requests.get(signatureUrl,headers=headers).content
    # f = open('font'+'.jpg','wb')
    # f.write(signature)
    print('生成成功,请点击下面的地址浏览')
    print(signatureUrl)






start()
# root = Tk()
# root.title('个性签名生成器')
# root.geometry('450x100+600+100')
# label = Label(root,text='请输入你的名字：',font=('微软雅黑',12))
# label.grid(row=0,column=0)
#
# entry = Entry(root,font=('微软雅黑',12),width=32)
# entry.grid(row=0,column=1)
#
# button = Button(root,font=('微软雅黑',12),text='点击生成个性签名',command=start)
# button.grid(row=1,columnspan=2)
#
#
# root.mainloop()