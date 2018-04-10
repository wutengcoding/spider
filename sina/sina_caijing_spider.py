from utils.spider_util import *

def parse_article_detail(detail_url):
    print('parse_detail_url is ' + detail_url)
    doc = pq(detail_url)
    return doc('div[class="article"]')('p')

if __name__ == '__main__':
    xinlang_caijing = "http://finance.sina.com.cn/"
    xinlang_caijing_html = get_search_result_by_url(xinlang_caijing)
    doc = pq(xinlang_caijing_html)
    for item in doc('div[id=blk_hdline_01]')('h3')('a').items():
        logging.info("标题:\t" + item.text() + ' url: \t' + item.attr("href"))
        detail_html = get_search_result_by_url(item.attr("href"))
        doc = pq(detail_html)
        logging.info(doc('div[id="artibody"]').text())