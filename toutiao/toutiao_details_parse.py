#coding="utf-8"
import os

from utils.spider_util import *
def parse_article_detail(detail_url):
    print('parse_detail_url is ' + detail_url)
    doc = pq(detail_url)
    return doc('div[class="article"]')('p')

def init_index_html(url):
    index_html = execute_script(url)
    with open('test.index', 'w', encoding="utf-8") as f:
        f.write(index_html)
    return index_html

if __name__ == '__main__':
    details_url =  "https://www.toutiao.com/a6540567317728723470/"
    detail_html = execute_script(details_url)
    doc = pq(detail_html)
    print(str(doc('div[class="article-content"]')('p').text()).strip())
    print(str(doc('div[class="article-content"]')).strip())

    # for item in doc('div[class="single-mode-rbox-inner"]')('div[class="title-box"]')('a').items():
    #     print(item.text(), item.attr("href"))