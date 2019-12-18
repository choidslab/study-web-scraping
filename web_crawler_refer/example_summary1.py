import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get("https://beomi.github.io/beomi.github.io_old/")
html = req.text
soup = BeautifulSoup(html, "html.parser")
titles = soup.select('h3 > a')  # css selector를 이용하여 html tag 요소 검색

data = {}  # json 파일에 데이터를 저장하기 위해 dict 타입 변수 생성

for title in titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_f:
    json.dump(data, json_f)
