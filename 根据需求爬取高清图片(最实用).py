# _*_ coding:utf-8 _*_
import requests
import re
import os

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}


def everyurl(j,name):
    namedict = {'风景':'fengjing','动漫':'dongman','美女':'meinv','创意':'chuangyi','卡通':'katong','汽车':'qiche','游戏':'youxi','可爱':'keai','明星':'mingxing','建筑':'jianzhu','植物':'zhiwu','静物':'jingwu','动物':'dongwu','影视':'yingshi','车模':'chemo','体育':'tiyu','品牌':'pinpai','星座':'xingzuo','美食':'meishi','节日':'jieri','其他':'qita'}
    for i in namedict:
        if name == i:
            return 'http://desk.zol.com.cn/' + namedict[i] + '/1920x1080/' +str(j)+ '.html' 

def get_id(url):
    pat = '<li class="photo-list-padding"><a class="pic" href="/.*?/(.*?)_2.html" target="_blank" hidefocus="true">'
    try:
        response = requests.get(url,headers=header).text
        idlist = re.compile(pat).findall(response)
    except:
        pass
    return idlist



def get_gaoqingurl(j,name):
    ls = []
    idlist = get_id(everyurl(j,name))
    for i in idlist:
        url = 'http://desk.zol.com.cn/bizhi/' + i + '_2.html'
        response = requests.get(url,headers=header).text
        pat = '<img .*?144x90(.*?).jpg" width="144" height="90"'
        gaoqingls = re.compile(pat).findall(response)
        ls.append(gaoqingls)
    return ls



def download(k,j,name):
    path = 'D:\爬虫\分类图片\\' + name + '图片'
    d = os.path.exists(path)
    if not d:
        os.mkdir(path)
        os.chdir(path)
    all_list = get_gaoqingurl(j,name)
    for ls in all_list:
        for l in ls:
            f = open(path + '\\' + str(k) + '.jpg', 'wb')
            url = 'https://desk-fd.zol-img.com.cn/t_s1920x1080' + l + '.jpg'
            pic = requests.get(url,headers=header).content
            f.write(pic)
            print('正在下载第{}张'.format(k))
            k += 1
    f.close()
    print('第{}页下载完-------------------'.format(j))
    return k





namels = ['风景','动漫','美女','创意','卡通','汽车','游戏','可爱','明星','建筑','植物','静物','动物','影视','车模','体育','品牌','星座','美食','节日','其他']
print('、'.join(namels))

name = input('请输入类别：')  #设置页数
k = 1
for j in range(1,83):
    l=download(k,j,name)
    k = 0
    k += l
