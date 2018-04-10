#coding="utf-8"
import urllib.request
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
import time
import re
import json
def get_logger(filename):
    import logging
    fh = logging.FileHandler(filename, encoding="utf-8")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fm=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    logger.addHandler(fh)
    fh.setFormatter(fm)
    return logger
    # logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO, filename=filename)
    # logging.FileHandler.encoding="utf-8"
    # return logging

def get_search_result_by_url(search_url):
    # 爬虫伪装头部设置
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    # 设置操作超时时长
    timeout = 5
    # 爬虫模拟在一个request.session中完成
    s = requests.Session()
    return s.get(search_url, headers=headers, timeout=timeout).content

# 使用webdriver 加载公众号主页内容，主要是js渲染的部分
def get_selenium_js_html(url):
    browser = webdriver.PhantomJS(executable_path=r'D:\applications\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    browser.get(url)
    time.sleep(3)
    # 执行js得到整个页面内容
    html = browser.execute_script("return document.documentElement.outerHTML")
    browser.close()
    return html