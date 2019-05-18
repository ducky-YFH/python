import requests
import re
import json
from lxml import etree
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}


def login():
    codeurl = 'https://www.douban.com/'
    codresponse = requests.get(codeurl,headers=headers).text
    pat = '<input type="hidden" name="captcha-id" value="(.*?):en"/>'
    code = re.compile(pat).findall(codresponse)
    captcha_id = ''.join(code)
    code_pic = 'https://www.douban.com/misc/captcha?id=' +captcha_id+ ':en&size=s'
    print(code_pic)
    ID = captcha_id+":en"
    codeID = input('请输入验证码：')
    url = 'https://www.douban.com/accounts/login'
    data = {
        'captcha-solution': codeID,
        'form_email':'17876383171',
        'form_password':'hhh2018hhh',
        'source':'index_nav',
        'captcha-id':ID
    }
    response = requests.post(url,data=data,headers=headers).text
    print(response)


login()



