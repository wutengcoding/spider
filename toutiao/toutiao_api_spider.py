# -*- coding:utf-8 -*-
import requests
import json
import time
import math
import hashlib
from utils.spider_util import *

logger = get_logger("api_spider.log")
def getASCP():
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()

    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS,CP

    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o + 3] + a[o]

    AS = 'A1' + s + e[-3:]
    CP = e[0:3] + r + 'E1'
    print("AS:"+AS,"CP:"+CP)
    return AS,CP


def get_signature():
    return execute_script("https://www.toutiao.com/ch/news_finance/", "return window.TAC.sign(0)")

def get_url(max_behot_time,AS,CP,sig):
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_finance&utm_source=toutiao&widen=1' \
           '&max_behot_time={0}' \
           '&max_behot_time_tmp={0}' \
           '&tadrequire=true' \
           '&as={1}' \
           '&cp={2}&_signature={3}'.format(0,AS,CP,sig)

    print(url)
    return url

def get_item(url):
    cookies = {"tt_webid":"6548654810030999043"
               }
    headers = {'User-Agent': user_agent}

    wbdata = requests.get(url,  headers=headers, cookies=cookies).content
    wbdata2 = json.loads(wbdata)
    data = wbdata2['data']
    print(data)
    for news in data:
        title = news['title']
        news_url = news['source_url']
        news_url = "https://www.toutiao.com"+news_url
        news_label = news.get('label', '-1')

        logger.info("%s\t%s\t%s" %(title,news_url, news_label))

    next_data = wbdata2['next']
    next_max_behot_time = next_data['max_behot_time']
    print("next_max_behot_time:{0}".format(next_max_behot_time))
    return next_max_behot_time


refresh = 4
sig = get_signature()
print(sig)
for x in range(0,refresh+1):
    print("第{0}次：".format(x))
    max_behot_time = 0

    AS,CP = getASCP()
    url = get_url(max_behot_time,AS,CP,sig)
    next_max_behot_time = get_item(url)
    time.sleep(1)