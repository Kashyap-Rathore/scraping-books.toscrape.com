import logging
from app import Books

logger= logging.getLogger('scraper.menu')

def menu(choice : int):
    while(choice != 4):
        if choice == 1:
            FindHighRatedBooks()
            input()
            choice = int(input("\nEnter the choice:\n1. FindHighRatedBooks\n2. FindCheapBooks\n3. NextBook\n4. Quit\n"))
            menu(choice)
        if choice == 2:
            FindCheapBooks()
            input()
            choice = int(input("\nEnter the choice:\n1. FindHighRatedBooks\n2. FindCheapBooks\n3. NextBook\n4. Quit\n"))
            menu(choice)
        if choice == 3:
            NextBook()
            input()
            choice = int(input("\nEnter the choice:\n1. FindHighRatedBooks\n2. FindCheapBooks\n3. NextBook\n4. Quit\n"))
            menu(choice)





def FindHighRatedBooks():
    logger.info('Findng the best rated books.')
    high_rated_books = sorted(Books, key=lambda x: (x.rating, x.price))[:10]
    for book in high_rated_books:
        print(book)


def FindCheapBooks():
    logger.info('Findng the cheap books.')
    cheap_books = sorted(Books, key=lambda x: x.price)[:10]
    for book in cheap_books:
        print(book)

booksGenerator= (b for b in Books)

def NextBook():
    logger.info('Findng the next book.')
    print(next(booksGenerator))

choice= int(input("Enter the choice:\n1. FindHighRatedBooks\n2. FindCheapBooks\n3. NextBook\n4. Quit\n"))
menu(choice)