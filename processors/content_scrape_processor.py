from processors.processor import Processor
from utils import log_helper

log = log_helper.get_logger("ContentScrapeProcessor")


class ContentScrapeProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        log.info("Processing begun")

        log.info("Processing complete")
