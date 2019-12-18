import requests
from bs4 import BeautifulSoup


req = requests.get("https://beomi.github.io/beomi.github.io_old/")
html = req.text

# header = req.headers
# status = req.status_code
# is_ok = req.ok

# BeautifulSoup 객체는 <tag></tag>로 구성된 html 요소를 Python이 이해할 수 있는 형태로 변환한 정보를 갖고 있는 객체이다.
soup = BeautifulSoup(html, "html.parser")
titles = soup.select('h3 > a')  # css selector를 이용하여 html tag 요소 검색
for title in titles:
    # print(title.text)
    print(title.get('href'))

