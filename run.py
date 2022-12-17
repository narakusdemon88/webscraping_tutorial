import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

    for url in url_lst:

        driver = webdriver.Firefox()
        driver.get(url)

        # get elements using Selenium
        a_links = driver.find_elements_by_xpath("a")

        driver.close()

        # convert to bs4 element and crawl as usual here
        page = Soup(driver.page_source, features="html.parser")

        for links in page.findAll("a"):
            print(links)
