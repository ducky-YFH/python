import requests
import re
import os
from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}


def get_url(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
        else:
            return None
    except:
        return None
    return html


def get_content(html):
    ls = []
    peoplels = []
    pinglunls = []
    titlepat = '<a href="/films/.*?" title="(.*?)" class="image-link"'
    peoplepat = '<p class="star">(.*?)</p>'
    datepat = '<p class="releasetime">(.*?)</p>'
    pinglunpat = '<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>'

    title = re.compile(titlepat).findall(html)
    people = re.compile(peoplepat, re.S).findall(html)
    date = re.compile(datepat).findall(html)
    pinglun = re.compile(pinglunpat).findall(html)
    ls.append(title)
    for j in people:
        peoplels.append(j.replace('\n', '').strip())
    ls.append(peoplels)
    ls.append(date)
    for i in pinglun:
        pinglunls.append(''.join(i))
    ls.append(pinglunls)
    return ls


def main():
    path = 'D:\爬虫\猫眼电影评分前100'
    e = os.path.exists(path)
    if not e:
        os.mkdir(path)
        os.chdir(path)
    f = open(path + '\\' + '猫眼电影评分前100部' + '.txt', 'a', encoding='utf-8')

    n = 0
    for i in range(10):
        url = 'http://maoyan.com/board/4?' + 'offset=' + str(i) + '0'
        print(url)
        content = get_content(get_url(url))
        for i in range(10):
            n += 1
            k = '排名' + str(n) + '：' + '《' + content[0][i] + '》  ' + content[1][i] + '      ' + content[2][
                i] + '      ' + '评分:' + content[3][i] + '\n'
            f.write(k + '\n')


if __name__ == '__main__':
    main()
