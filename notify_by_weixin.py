#!/usr/bin/python
#-*- coding:utf-8 -*-

import urllib2
import json
import sys
import memcached

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

corpid = 'wxce6473210d1212ee'
corpsecret = 'Wt7aVAir4iSsTI4batmOb6xJHgiBagHx-D6uzvl2gNR4B0FRFAK2BGvEkTK4cGAf'
    
#创建获取AccessToken的方法
def gettoken(corp_id,corp_secret):
    token = memcached.getAccessToken()
    if token:
        return token
    
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corp_id + '&corpsecret=' + corp_secret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    memcached.setAccessToken(token)
    return token

#这里是发送消息的方法
def senddata(access_token,notify_str):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    #我传入的参数是一段字符串每个信息用separator连起来，只要再用字符串的split("separator")方法分开信息就可以了。
    notifydata = notify_str.split("|")
    user = notifydata[0]
    cationtype = notifydata[1]
    name = notifydata[2]
    state = notifydata[3]
    address = notifydata[4]
    output = notifydata[5]
    datatime = notifydata[6]
    content = ' [擦汗] [擦汗]  Nagios 警报   [擦汗] [擦汗]  \n\n 类型 : ' + cationtype + '\n 主机名 : ' + name + '\n 状态 : ' + state + '\n IP 地址 : ' + address + '\n[猪头] 日志 : ' + output + '\n\n[瓢虫] 时间 : ' + datatime + '\n'
    send_values = {
        "touser":user,
        "msgtype":"text",
        "agentid":"1",
        "text":{
            "content":content
            },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False).encode()

    #设置为非ascii解析，使其支持中文
    send_request = urllib2.Request(send_url, send_data)
    response = urllib2.urlopen(send_request)
    #这个是返回微信公共平台的信息，调试时比较有用
    msg = response.read()
    return msg

def test():
    #我编辑的脚本是要获取nagios传入的一段参数的（字符串），下面这条代码是获取执行脚本后获取的第一个参数（经测试nagios只能传入一个参数进python，所以把所有包括用户名跟报警主机报警信息放进一个字符串里）
    notifystr = str(sys.argv[1])
    accesstoken = gettoken(corpid,corpsecret)
    msg = senddata(accesstoken,notifystr)
    print(msg)

if __name__ == "__main__":
    test()

