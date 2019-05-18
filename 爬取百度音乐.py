import json
import requests
import re
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_songurl(songer):
    url = 'http://music.taihe.com/search?'
    key = {'key':songer}
    response = requests.get(url,headers=headers,params=key)
    response.encoding='utf-8'
    response=response.text
    return response

def get_id(response):
    pat = 'sid&quot;:(.*?),'
    IDS = re.compile(pat).findall(response)
    return IDS


def get_music(songer,IDS):
    path = 'D:/爬虫/百度音乐' +'//'+ songer
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    for id in IDS:
        jsurl = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=' +id+ '&from=web&_=1540458761054'
        jsresponse = requests.get(jsurl,headers=headers).text
        js = json.loads(jsresponse)
        title=js['songinfo']['title']
        file_link=js['bitrate']['file_link']
        music = requests.get(file_link,headers=headers).content
        with open(path +'//'+ title+ '.mp3','wb') as f:
            f.write(music)
            f.close()
        print('下载：%s---成功'%title)



songer = input('请输入你喜欢的明星：')
response = get_songurl(songer)
IDS=get_id(response)
get_music(songer,IDS)