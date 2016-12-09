import json

from args.options import Options
from processors.processor import Processor
from utils import log_helper, scrape_helper

log = log_helper.get_logger("TermScrapeProcessor")


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

            term_set = set()
            log.info("Working on index term " + index_term)
            num = 1

            while True:
                term_set_length = len(term_set)

                url = self.root_url + index_term + "/?page=" + str(num)
                log.info("Parsing page at " + url)

                links = scrape_helper.get_term_links_from_page(url)

                for link in links:
                    term_set.add(self.domain + link['href'])

                num += 1

                if term_set_length == len(term_set):
                    break

            for term in term_set:
                print(term, file=f)

        f.close()

        log.info("Processing complete")
