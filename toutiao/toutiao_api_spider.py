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



def get_url(max_behot_time,AS,CP):
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_finance&utm_source=toutiao&widen=1' \
           '&max_behot_time={0}' \
           '&max_behot_time_tmp={0}' \
           '&tadrequire=true' \
           '&as={1}' \
           '&cp={2}&_signature=acd'.format(max_behot_time,AS,CP)

    print(url)
    return url

def get_item(url):
    cookies = {"tt_webid":"6540547118872249859",
               "UM_distinctid": "1629053595141a-0dfc077bb0cb42-4446062d-100200-1629053595250c",
               "uuid": "w:1f13cfb4b5e64ce195e83efc214c4349"
               }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}

    wbdata = requests.get(url,headers=headers, cookies = cookies).content
    wbdata2 = json.loads(wbdata)
    data = wbdata2['data']
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


refresh = 50
for x in range(0,refresh+1):
    print("第{0}次：".format(x))
    if x == 0:
        max_behot_time = 0
    else:
        max_behot_time = next_max_behot_time
        print (max_behot_time)

    AS,CP = getASCP()
    url = get_url(max_behot_time,AS,CP)
    next_max_behot_time = get_item(url)
    time.sleep(1)