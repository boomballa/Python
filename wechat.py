#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 下午4:52
# @Author  : Liujiaqi
# @Site    :
# @File    : wechat.py.py
# @Software: PyCharm

import requests,sys,json
#import urllib3
#urllib3.disable_warnings()

def GetToken(Corpid,Secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid":Corpid,
        "corpsecret":Secret
    }
    r = requests.get(url=Url,params=Data,verify=False)
    Token = r.json()['access_token']
    print Token
    return Token

def SendMessage(Token,User,Agentid,Subject,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": User,                                 # 企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        #"totag": 3,                                    # 企业号中的部门id，群发时使用。
        "msgtype": "text",                              # 消息类型。
        "agentid": Agentid,                             # 企业号中的应用id。
        "text": {
            "content": Subject + '\n' + Content
        },
        "safe": "0"
    }
    r = requests.post(url=Url,data=json.dumps(Data),verify=False)
    return r.text


if __name__ == '__main__':
    User = sys.argv[1]                                                              # zabbix传过来的第一个参数
    Subject = sys.argv[2]                                                           # zabbix传过来的第二个参数
    Content = sys.argv[3]                                                           # zabbix传过来的第三个参数

    Corpid = "wwefc3bf9b4e40228a"                                                   # CorpID是企业号的标识
    Secret = "yhevly2MteZ0BYhEcv1PSAfXHgx2voTgdANrC5JtKuY"                          # Secret是管理组凭证密钥
    Agentid = "1000002"                                                                   # 应用ID

    Token = GetToken(Corpid, Secret)
    Status = SendMessage(Token,User,Agentid,Subject,Content)
