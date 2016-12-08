import requests

from utils import log_helper
from processors.processor import Processor
from args.options import Options
from bs4 import BeautifulSoup

log = log_helper.get_logger("AmazonReviewProcessor")


class ScrapeProcessor(Processor):

    def process(self):

        log.info("Processing begun")

        url = 'http://www.investopedia.com/terms/a/'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'lxml')

        log.info(soup)

        log.info("Processing complete")
