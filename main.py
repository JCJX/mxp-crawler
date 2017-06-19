
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except(HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.tbody.td
    except ArithmeticError as e:
        return None
    return title
title = getTitle("http://www.880qp.net/AdminV2/Record/GameMoneyRecords.aspx")
if title == None:
    print("出错了")
else:
    print(title)

