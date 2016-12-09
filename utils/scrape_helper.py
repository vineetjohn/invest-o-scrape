import requests
from bs4 import BeautifulSoup


def get_term_links_from_page(url):

    response = requests.get(url, allow_redirects=True)

    soup = BeautifulSoup(response.content, 'lxml')
    layout_page_content = \
        str(BeautifulSoup(str(soup.find(id="Content")), 'lxml').findAll("div", {"class": "layout-page"}))

    links = BeautifulSoup(layout_page_content, 'lxml').findAll("a", {"data-cat": "content_list"})

    return links


def get_content_from_termpage(url):

    response = requests.get(url, allow_redirects=True)

    page_soup = BeautifulSoup(response.content, 'lxml')

    term = \
        page_soup\
        .find_all("div", {"class": "layout-title only-fontsize-title title-space"})[0]\
        .find_all("h1")[0].get_text()

    content_box = str(page_soup.find_all("div", {"class": "content-box content-box-term"})[0])

    paras = BeautifulSoup(content_box, 'lxml')
    definition = str(paras.find_all("p")[0].get_text())
    break_down = str(paras.find_all("p")[1].get_text())

    term_object = dict()
    term_object['term'] = term
    term_object['definition'] = definition
    term_object['break_down'] = break_down

    return term_object
