import re
import requests
from lxml import etree
import pymysql


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}

def get_title(url):
    lxml = requests.get(url,headers=headers).text
    selector = etree.HTML(lxml)
    title = selector.xpath('//div[@class="book-mid-info"]/h4/a/text()')
    return title

def get_autor(url):
    lxml = requests.get(url,headers=headers).text
    selector = etree.HTML(lxml)
    autor = selector.xpath('//p[@class="author"]/a[1]/text()')
    return autor

def get_leibie(url):
    lxml = requests.get(url, headers=headers).text
    selector = etree.HTML(lxml)
    lei = selector.xpath('//p[@class="author"]/a[2]/text()')
    return lei

def main(url):
    try:
        title = get_title(url)
        aut = get_autor(url)
        lei = get_leibie(url)
        conn = pymysql.connect(host='localhost',db='douban',user='root',passwd='123456',charset='utf8',use_unicode=True)
        cursor = conn.cursor()
        for i in range(len(title)):
            cursor.execute("""insert into story(title,autor,leibie)value (%s,%s,%s)""",(title[i], aut[i], lei[i]))
            print('成功')
    except Exception as e:
        print('wrong')
    conn.commit()
    conn.close()


if __name__== '__main__':
    url = 'https://www.qidian.com/all'
    for i in range(1,200):
        url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=' + str(i)
        main(url)

