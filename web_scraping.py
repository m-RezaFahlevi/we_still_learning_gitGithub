from urllib.request import urlopen
#Ohh..no...the_package_require_for_this_code
#has_been_deleted
from urllib.error import URLError

#I think, it is good to write a program in the term of
#Object-Oriented Programming :)
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
