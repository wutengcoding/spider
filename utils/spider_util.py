#coding="utf-8"
import urllib.request
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
import time
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument('--headless')
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'd:\applications\chromedriver.exe')
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
def execute_script(url, cmd="return document.documentElement.outerHTML"):


    driver.get(url)
    html = driver.execute_script(cmd)
    # driver.close()
    return html

if __name__ == '__main__':
    print(execute_script("https://www.toutiao.com/ch/news_finance/", "return window.TAC.sign(0)"))
