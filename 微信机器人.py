import itchat
import requests
import re
from tkinter import *


def gethtmltext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture'])
#定义自动回复
def text_reply(msg):
    if not msg['FromUserName'] == Name['大黑帅']:
        url = "http://www.tuling123.com/openapi/api?key=8008b8f3f7c740f29ba4691ce0a318e8&info="
        url = url + msg['Text']
        html = gethtmltext(url)
        message = re.findall(r'\"text\"\:\".*?\"', html)
        reply = eval(message[0].split(':')[1])
        return reply

if __name__ == '__main__':
    #  通过itchat扫码登录微信网页版
    itchat.auto_login()
    #  获取所有微信好友的信息
    friends = itchat.get_friends(update=True)[0:]
    #  使用字典存放好友昵称与用户名
    Name = {}
    #  好友昵称
    Nic = []
    #  好友用户名
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    itchat.run()

