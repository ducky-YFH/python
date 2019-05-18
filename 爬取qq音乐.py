import requests
import json
import os


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_mid(url):
    response = requests.get(url,headers=headers).text
    response = response.replace('MusicJsonCallback5963715333145192(', '')
    response = response[0:-1]
    js = json.loads(response)
    list = js['data']['song']['list']
    # print(list)
    dict = {}
    for i in list:
        mid=i['file']['media_mid']
        title=i['name']
        dict[title] = mid
    return dict

def get_music(mid):
    music = {}
    for id in mid:
        try:
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg? &g_tk=1796449428 &loginUin=508766975&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%229662259017%22%2C%22songmid%22%3A%5B%22' + mid[id] + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%22508766975%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A508766975%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D'
            jsresponse = requests.get(url, headers=headers).text
            js = json.loads(jsresponse)
            js2 = (js['req_0']['data']['midurlinfo'])
            for key in js2:
                vkey = key['purl']
                musiclink = 'http://musichy.tc.qq.com/amobile.music.tc.qq.com/'+vkey
                music[id] = musiclink
                #print(id)
                #print(musiclink)
        except:
            print('出错')
    return music


def download(music):
    path = 'D:/音乐'
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    for title in music:
        print(title)
    love = input('请输入你想下载的音乐(如果多首请用"、"分隔开)：')
    love = love.split('、')
    for title in music:
        if title in love:
            for i in love:
                f = open(path + '\\' + i + '.mp3','wb')
                last = requests.get(music[i],headers).content
                f.write(last)
                f.close()
                print('{}:下载成功'.format(i))
            break


def main():
    n = 1
    s = input('请输入你喜欢的明星或歌曲：')
    for page in range(1,6):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64653950969281607&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=' +str(page)+ '&n=20&w=' +s+ '&g_tk=5381&jsonpCallback=MusicJsonCallback5963715333145192&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        mid = get_mid(url)
        music = get_music(mid)
        print('-------------第{}页-------------'.format(n))
        download(music)
        n += 1


if __name__ == '__main__':
    main()