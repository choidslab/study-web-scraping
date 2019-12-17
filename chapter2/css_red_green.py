from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
# print(bsObj)

name_list = bsObj.findAll("span", {"class": "green"})  # css font color 'green'만 찾아서 출력
for name in name_list:
    print(name.get_text())
