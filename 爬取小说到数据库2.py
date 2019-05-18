import requests
from lxml import etree
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}



def get_title(url):
    response = requests.get(url,headers=headers)
    lxml = etree.HTML(response.text)
    title = lxml.xpath('//td[@class="td3"]/span/a[@class="jt"]/text()')
    return title


def get_autor(url):
    response = requests.get(url,headers=headers)
    lxml = etree.HTML(response.text)
    autor = lxml.xpath('//li[@class="zz"]/a/text()')
    return autor

def get_leibie(url):
    response = requests.get(url,headers=headers)
    lxml = etree.HTML(response.text)
    lei = lxml.xpath('//td[@class="td2"]/a/text()')
    return lei

def get_time(url):
    response = requests.get(url,headers=headers)
    lxml = etree.HTML(response.text)
    ls = lxml.xpath('//td[@class="td7"]/text()')
    time = []
    for i in range(1,31):
        time.append(ls[i])
    return time



def main(url):
    title = get_title(url)
    autor = get_autor(url)
    leibie = get_leibie(url)
    time = get_time(url)
    try:
        for i in range(len(title)):
            cursor.execute("""insert into story2(title,autor,leibie,time)value (%s,%s,%s,%s)""",(title[i],autor[i],leibie[i],time[i]))
            print('成功了')
    except Exception as e:
        print('失败了')


url = 'http://all.17k.com/lib/book/2_0_0_0_0_4_0_0_1.html'
get_time(url)


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', charset='utf8', db='douban')
    cursor = conn.cursor()
    for i in range(1,700):
        url = 'http://all.17k.com/lib/book/2_0_0_0_0_4_0_0_' +str(i)+ '.html'
        main(url)
    conn.commit()
    conn.close()