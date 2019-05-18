import requests
import re
import os

url = 'http://huaban.com/boards/favorite/beauty'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}



def get_url(s):
    if s == 1:
        url = 'http://www.win4000.com/wallpaper_191_0_10_2.html'
    if s == 2:
        url = 'http://www.win4000.com/wallpaper_192_0_10_2.html'
    if s == 3:
        url = 'http://www.win4000.com/wallpaper_194_0_10_2.html'
    if s == 4:
        url = 'http://www.win4000.com/wallpaper_195_0_10_2.html'
    if s == 5:
        url = 'http://www.win4000.com/wallpaper_197_0_10_2.html'
    return url


#获取每张图片对应的id列表
def find_ID(url):
    pat = '<a href="http://www.win4000.com/wallpaper_detail_(.*?).html" alt="'
    response = requests.get(url,headers=header).text
    Idlist = re.compile(pat).findall(response)
    return Idlist

#获取名字
def find_name(url):
    pat = ' ?>" title="(.*?)" target="_blank"'
    response = requests.get(url, headers=header).text
    Namelist = re.compile(pat).findall(response)
    return Namelist


#或得所在类型的每个link
def get_link():
    linklist = []
    for id in find_ID(get_url(s)):
        link = 'http://www.win4000.com/wallpaper_big_'+ id +'.html'
        linklist.append(link)
    return linklist


#获取高清壁纸的link
def get_piclink(linklist):
    piclink = []
    pat = '<a href="(.*?)" target = "_blank">'
    for url in linklist:
        response = requests.get(url,headers=header).text
        link = re.compile(pat).findall(response)
        piclink.append(link)
    return piclink


def download(namelist,linklist):
    for i in range(len(namelist)):
        path = 'D:\爬虫\高清图片\\' + namelist[i]
        D = os.path.exists(path)
        if not D:
            os.mkdir(path)
            os.chdir(path)
            n=0
            print('开始下载{}'.format(namelist[i]))
            for ls in linklist[i]:
                n+=1
                f=open(path +'\\'+ str(n) +'.jpg','wb')
                pic = requests.get(ls,headers=header).content
                f.write(pic)
                print('下载{}张成功'.format(n))
                f.close()
            print('下载成功')


print('1:游戏,2:卡通,3:军事基地,4:汽车壁纸,5:设计创意')
s = eval(input('请选择你喜欢的类型(1-5)数字:'))


download(find_name(get_url(s)),get_piclink(get_link()))