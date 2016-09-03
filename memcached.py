#!/usr/bin/python
#-*- coding:utf-8 -*-

import memcache

host=["121.40.226.188:11211"]
qy_token_key="PYTHON_QY_WEIXIN_ACCESS_TOKEN"

def get(key):
    mc = memcache.Client(host, debug=0)
    return mc.get(key)

def setAccessToken(token):
    mc = memcache.Client(host, debug=0)
    mc.set(qy_token_key, token, 3600)
    
def getAccessToken():
    return get(qy_token_key)
    
def test():
    mc = memcache.Client(host, debug=0)
    mc.set("QY_WEIXIN_ACCESS_TOKEN_1", "x", 3600)
    print mc.get("QY_WEIXIN_ACCESS_TOKEN_1")
    print mc.get("ADF")
    print getAccessToken()
    
if __name__ == "__main__":
    test()