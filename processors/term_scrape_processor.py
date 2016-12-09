import time
import requests
import json
from bs4 import BeautifulSoup

from processors.processor import Processor
from args.options import Options
from utils import log_helper

log = log_helper.get_logger("AmazonReviewProcessor")


class TermScrapeProcessor(Processor):

    def __init__(self):
        super().__init__()
        self.domain = "http://www.investopedia.com"
        self.root_url = self.domain + "/terms/"
        self.min_term_count = 100

    def process(self):

        log.info("Processing begun")

        with open(Options.args.term_indices_file_path) as indices_file:
            list_of_indices = json.load(indices_file)

        log.info("There are " + str(len(list_of_indices)) + " indices")

        f = open(Options.args.output_file_path, 'w')

        for index_term in list_of_indices:

            log.info("Working on index term " + index_term)
            num = 1
            term_count = 100

            while term_count >= self.min_term_count:
                url = self.root_url + index_term + "/?page=" + str(num)
                log.info("Parsing page at " + url)

                response = requests.get(url, allow_redirects=True)
                time.sleep(1)

                soup = BeautifulSoup(response.content, 'lxml')
                layout_page_content = \
                    str(BeautifulSoup(str(soup.find(id="Content")), 'lxml').findAll("div", {"class": "layout-page"}))

                links = BeautifulSoup(layout_page_content, 'lxml').findAll("a", {"data-cat": "content_list"})

                term_count = len(links)
                for link in links:
                    # log.info(self.domain + link['href'])
                    print(self.domain + link['href'], file=f)

                num += 1

        f.close()

        log.info("Processing complete")
