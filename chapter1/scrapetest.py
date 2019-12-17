from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs_obj = BeautifulSoup(html.read(), "html.parser")
print(bs_obj)
print(bs_obj.h1)
