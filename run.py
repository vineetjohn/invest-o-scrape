import sys

from args.options import Options
from argparse import ArgumentParser
from processors.term_scrape_processor import TermScrapeProcessor
from processors.content_scrape_processor import ContentScrapeProcessor
from exceptions.CmdLineException import CmdLineException
from utils import log_helper

log = log_helper.get_logger("run")


def parse_args(argv):

    parser = ArgumentParser(prog="Investopedia Term Scraper")
    parser.add_argument('--mode', metavar='Term Scrape / Content Scrape', type=str)
    parser.add_argument('--term_indices_file_path', metavar='Term Indices for Investopedia', type=str)
    parser.add_argument('--term_list_file_path', metavar='Term List filepath', type=str)
    parser.add_argument('--output_file_path', metavar='Output File Path', type=str)

    Options.args = parser.parse_args(argv, namespace=Options)


def validate_args(args):

    if args.mode == 'term-scrape':

        if not args.term_indices_file_path:
            msg = "'term-scrape' mode requires 'term_indices_file_path'"
            log.error(msg)
            raise CmdLineException(msg)

    elif args.mode == 'content-scrape':
        pass

    else:
        msg = "Invalid arg for mode. Use either 'term-scrape' or 'content-scrape'"
        log.error(msg)
        raise CmdLineException(msg)

    if not args.output_file_path:
        msg = "'output_file_path' is a required arg"
        log.error(msg)
        raise CmdLineException(msg)


def main(argv):

    parse_args(argv)
    validate_args(Options.args)

    if Options.args.mode == 'term-scrape':
        processor = TermScrapeProcessor()
    else:
        processor = ContentScrapeProcessor()

    processor.process()


if __name__ == "__main__":
    main(sys.argv[1:])
