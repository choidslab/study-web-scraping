from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:  # 선택한 첫 번째 행을 제외한 나머지 행 값을 반환
    print(sibling)
