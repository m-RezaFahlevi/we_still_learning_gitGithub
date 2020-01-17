from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

def get_url(some_url):
    try:
        html = urlopen('https://httpbin.org/ip')
    except HTTPError:
        print("URL not found")
        print(HTTPError)
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html5lib')
        getTag = bs.body.get_text()
    except URLError:
        print(URLError)
        return None
    except AttributeError:
        print('Tag not found maybe')
        print(AttributeError)
        return None
    return getTag

py_var = get_url('https://httpbin.org/ip')

print('Tag not found') if(py_var == None) else print(py_var)
