import json
from utils import scrape_helper

url = "http://www.investopedia.com/terms/1/10k-wrap.asp"

term_object = scrape_helper.get_content_from_termpage(url)

print(json.dumps(term_object))
