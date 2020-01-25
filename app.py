import requests
import logging
from pages.BookPage import BeautifulSoupContentFetcher


logging.basicConfig(format= '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger= logging.getLogger('scraping')

logger.info('Loading books list..')

get_page= requests.get(f'http://books.toscrape.com')
page_content= get_page.content
page_data= BeautifulSoupContentFetcher(page_content)

Books= page_data.TagFetcher

for i in range(1, page_data.PageFinder):
    get_page= requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
    page_content= get_page.content
    logger.debug('Creating BeautifulSoupContentFetcher from page content')
    page_data= BeautifulSoupContentFetcher(page_content)

    Books.extend(page_data.TagFetcher) #we are doing this so that all the information from all the pages get stored
