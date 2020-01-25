import re
import logging
from locator.BookLocator import BookLocator

logger= logging.getLogger('scraping.Book')

class BookParser:
    num_rating = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,parent):
        logger.debug(f'New Book parser created from `{parent}`.')
        self.parent= parent

    def __repr__(self):
        return f'\n<Book>\nName of book: {self.name}\nPrice of book: {self.price}\nRating of book: {self.rating}\nLink for book: {self.link}'

    @property
    def name(self):
        name = self.parent.select_one(BookLocator.NAME).attrs['title']
        logger.debug('Found book name {name}')
        return name

    @property
    def price(self):
        price = self.parent.select_one(BookLocator.PRICE).string
        pattern= '£([0-9]+\.[0-9]+)'
        matcher= re.search(pattern, price)
        logger.debug('Found book price `{matcher.group(1)}`.')
        return float(matcher.group(1))

    @property
    def rating(self):
        rating_class = self.parent.select_one(BookLocator.RATING).attrs['class']
        rating= [r for r in rating_class if r!= 'star-rating']
        rating_number= BookParser.num_rating.get(rating[0])
        logger.debug('Found book rating `{rating_number}`.')
        return rating_number

    @property
    def link(self):
        link = self.parent.select_one(BookLocator.LINK).attrs['href']
        return link