from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), "html.parser")
        html_title = bs_obj.h1
    except AttributeError as e:
        return None
    return html_title


if __name__ == "__main__":

    title = get_title('http://pythonscraping.com/pages/page1.html')
    if title is None:
        print("Title could not be found")
    else:
        print(title)
