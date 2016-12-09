from utils import scrape_helper

url = "http://www.investopedia.com/terms/1/"

links = scrape_helper.get_term_links_from_page(url)

print(links)
