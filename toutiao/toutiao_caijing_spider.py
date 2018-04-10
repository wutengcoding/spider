#coding="utf-8"
import os

from utils.spider_util import *
logger = get_logger("toutiao_caijing.log")
def parse_article_detail(detail_url):
    print('parse_detail_url is ' + detail_url)
    doc = pq(detail_url)
    return doc('div[class="article"]')('p')

def init_index_html(url):
    index_html = get_selenium_js_html(url)
    with open('test.index', 'w', encoding="utf-8") as f:
        f.write(index_html)
    return index_html

if __name__ == '__main__':
    index_url = "https://www.toutiao.com/ch/news_finance/"
    index_file = 'test.index'
    # index_html = get_search_result_by_url(xinlang_caijing)
    if os.path.exists(index_file):
        logger.info("Already has index html in local path")
        with open(index_file, encoding="utf-8") as f:
            index_html = f.read()
    else:
        logger.info("First time load index")
        index_html = init_index_html(index_url)
    doc = pq(index_html)
    for item in doc('div[class="y-left index-content"]')('a[class="link title"]').items():
        logger.info("标题:\t" + item.text() + ' url: \t' + item.attr("href"))

    exit(0)
    for item in doc('div[class="item-inner"]')('a[class="title"]').items():
        print("标题:\t" + item.text() + ' url: \t' + item.attr("href"))
        # detail_html = get_search_result_by_url(item.attr("href"))
        # doc = pq(detail_html)
        # logging.info(doc('div[id="artibody"]').text())