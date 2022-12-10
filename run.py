import requests
from bs4 import BeautifulSoup


class Website(object):
    def __init__(self, url):
        self.url = url

    @property
    def soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup


if __name__ == "__main__":
    """
    TODO:
        1. explain requests and bs4 library
        2. show .text, .find, .findAll
        3. .findAll("div")
        4. .findAll("div", class_="...")
        5. .findAll("a") --> .attrs
        6. make dictionary w/ values
        7. append to dataframe
        8. selenium
        9. convert selenium into bs4 instance
    """
    url_lst = ["http://localhost:3000/webcrawl_tutorial.html"]

    print("Hi")
