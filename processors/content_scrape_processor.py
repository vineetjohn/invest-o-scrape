import json

from processors.processor import Processor
from utils import log_helper, file_helper, scrape_helper
from args.options import Options

log = log_helper.get_logger("ContentScrapeProcessor")


class ContentScrapeProcessor(Processor):

    def __init__(self):
        super().__init__()

    def process(self):

        log.info("Processing begun")

        input_file_reader = file_helper.get_file_line_iterator(Options.args.term_list_file_path)
        output_file_object = open(Options.args.output_file_path, 'w')

        log.info("Reading and processing terms list")
        for line in input_file_reader:
            try:
                term_dict = scrape_helper.get_content_from_termpage(line.strip())
                print(json.dumps(term_dict), file=output_file_object)
            except Exception as e:
                log.error("Error while scraping content from url " + line)

        output_file_object.close()

        log.info("Processing complete")
