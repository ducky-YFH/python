import requests
import re
import os
import json

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400"}


def move_type():
    url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
    response = requests.get(url,headers=headers).text
    pat = '&type=(.*?)=100:90&action=">(.*?)</a>'
    ls = re.compile(pat).findall(response)
    dict = {}
    for i in ls:
        dict[i[1]] = i[0]
    return dict


def get_move():
    path = 'D:/爬虫/豆瓣电影分类排行榜'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    dict = move_type()
    for move in dict:
        n = 1
        link = dict[move]
        f = open(path+'//'+move+'.txt','a',encoding='utf-8')
        for j in range(0,800,20):
            url = 'https://movie.douban.com/j/chart/top_list?type=' +link+ '=100:90&action=&start=' +str(j)+ '&limit=20'
            response = requests.get(url,headers).text
            if response == '[]':
                break
            else:
                js = json.loads(response)
                for i in js:
                    score = i['score']
                    title = i['title']
                    date = i['release_date']
                    type = i['types'] #list
                    address = i['regions'] #list
                    actor = i['actors'] #list
                    type = ','.join(type)
                    address = ','.join(address)
                    actor = ','.join(actor)
                    f.write('排名{}：'.format(n)+'《{}》'.format(title)+'     类型：'+type+'     主演：'+actor+'    上映时间：'+date+'({})'.format(address)+'     评分：'+score+'\n'+'\n')
                    n += 1
                    print(title+'下载成功')
        f.close()



get_move()







