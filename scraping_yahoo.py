import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    r = requests.get('http://baseball.yahoo.co.jp/npb/stats/batter?series=1')
    print(r.status_code)
    print(r.encoding)
    print(r.headers)
    print(r.text)


# html = urllib2.urlopen("http://example.com")
#
# soup = BeautifulSoup(html)
