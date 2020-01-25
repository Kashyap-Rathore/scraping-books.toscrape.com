import re
from bs4 import BeautifulSoup
from locator.BookPageLocator import BookPageLocator
from Parser.Book import BookParser
import logging

logger= logging.getLogger('scraping.BookPage')


class BeautifulSoupContentFetcher():
    def __init__(self,page_content):
        logger.debug('Parsing page content using BeautifulSoup')
        self.soup= BeautifulSoup(page_content, 'html.parser')

    @property
    def TagFetcher(self):
        locator= BookPageLocator.LOCATOR
        book_tag= self.soup.select(locator)
        logger.debug(f'Finding all books in the page using `{BookPageLocator.LOCATOR}`.')
        return [BookParser(e) for e in book_tag]

    @property
    def PageFinder(self):
        page_content= self.soup.select_one(BookPageLocator.PAGE).string
        logger.info(f'Finding all pages using `{page_content}`.')
        page_pattern= 'Page [0-9]+ of ([0-9]+)'
        expression= re.search(page_pattern,page_content)
        pages= int(expression.group(1))
        logger.debug('Extracted number of pages as int: `{pages}`.')
        return int(pages)