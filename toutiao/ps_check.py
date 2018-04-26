import requests
for i in range(200):
    r = requests.get("http://diviner.jd.com/diviner?p=619191&hi=%7B%22pi%22:%22home%22,%22ci%22:%220%22,%22did%22:%5B619191%5D%7D&lim=100&lid=1&ec=utf-8&fe=101&pin=&uuid=&&fmt=dbg&directip=10.190.88.27:9090")
    if "zookeeper" not in str(r.content):
        print(r.content)
    else:
        print(i, "is ok")
