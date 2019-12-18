import re

from urllib.request import urlopen
from bs4 import BeautifulSoup


pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:  # 새로운 page인 경우
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)  # 새로운 page url 추가
                getLinks(newPage)  # recursion

getLinks("")


"""
  - Python에서는 재귀호출을 1,000회로 제한됨
  - 크롤러를 개발 시 주의
"""