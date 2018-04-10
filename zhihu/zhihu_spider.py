from utils.spider_util import *

def parse_article_detail(detail_url):
    print('parse_detail_url is ' + detail_url)
    doc = pq(detail_url)
    return doc('div[class="article"]')('p')


def login():
    import json
    with open('cookie.txt') as f:
        cookie_data = json.loads(f.read())
        print(cookie_data)
        import requests
        r = requests.post('http://zhihu.com', cookies=cookie_data)
        print(r.content)
    login_url = "https://www.zhihu.com/signup?next=%2F"
    data = {
        'email': 'bruceteng116@gmail.com',
        'password': 'wt030105',
        'rememberme': "true",
    }



    zhihu_login_html = get_search_result_by_url(login_url)
    doc = pq(zhihu_login_html)
    if doc("div[class='Captcha-chineseOperator']") is not None:
        print("has getcha")
    else:
        print("no getcha")

if __name__ == '__main__':
    login()
    # for item in doc('div[id=blk_hdline_01]')('h3')('a').items():
    #     logging.info("标题:\t" + item.text() + ' url: \t' + item.attr("href"))
    #     detail_html = get_search_result_by_url(item.attr("href"))
    #     doc = pq(detail_html)
    #     logging.info(doc('div[id="artibody"]').text())