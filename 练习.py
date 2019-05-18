import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}
def get_html(url):
    html = requests.get(url,headers=headers)
    html.encoding='utf-8'
    return html.text

def get_name(html):
    soup = BeautifulSoup(html,'lxml')
    namels = soup.select('a[target="_blank"] em')
    return namels


def get_money(html):
    pat = '<em>￥</em><i>(.*?)</i></strong>'
    moneyls = re.compile(pat).findall(html)
    return moneyls

def get_comment(html):
    pat = '">(.*?)</a>条评价</strong>'
    commentls = re.compile(pat).findall(html)
    return  commentls


def main():
    n = input('请输入商品名称:')
    url = 'https://search.jd.com/Search?keyword=' +n+ '&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=' +n+ '&psort=3&click=0'
    html = get_html(url)
    namels = get_name(html)

    moneyls = get_money(html)
    commentls = get_comment(html)
    for i in range(len(moneyls)):
        print ('名称：' + namels[i]  +'   价钱：'+  moneyls[i] +'   评论：' +commentls[i])



if __name__ == '__main__':
    main()