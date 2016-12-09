import sys

from args.options import Options
from argparse import ArgumentParser
from processors.term_scrape_processor import TermScrapeProcessor


def parse_args(argv):
    """
    Parses command line arguments form an options object
    :param argv:
    :return:
    """
    parser = ArgumentParser(prog="Investopedia Term Scraper")
    parser.add_argument('--term_indices_file_path', metavar='Term Indices for Investopedia', type=str)
    parser.add_argument('--output_file_path', metavar='Output File Path', type=str)

    Options.args = parser.parse_args(argv, namespace=Options)


def main(argv):
    """
    Main function to kick start execution
    :param argv:
    :return: null
    """
    parse_args(argv)
    processor = TermScrapeProcessor()
    processor.process()


if __name__ == "__main__":
    main(sys.argv[1:])
