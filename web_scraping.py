from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

#function scrape the url
#def getTitle(someUrl):
#    try:
#        html = urlopen(someUrl)
#    except HTTPError:
#        return None
#    try:
#        bs = BeautifulSoup(html.read(), "html5lib")
#        title = bs.body.h
#   except AttributeError:
#       return None
#    return title

#pyVar = getTitle('http://www.pythonscraping.com/pages/page1.html')

#print("title could not be found") if pyObject == None else print(pyObject)

#Object Oriented Style
class WebScraping:
    def __init__(self, someUrl):
        self.someUrl = someUrl

    def getUrl(self):
        try:
            html = urlopen(self.someUrl)
        except HTTPError:
            return None
        try:
            bs = BeautifulSoup(html.read(), "html5lib")
            title = bs.body.h
        except AttributeError:
            return None
        return title

pyObject = WebScraping('http://www.pythonscraping.com/pages/page1.html')
print("Title could not be found") if pyObject.getUrl() == None else print(pyObject.getUrl())
