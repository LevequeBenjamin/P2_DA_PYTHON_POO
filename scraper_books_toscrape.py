#! /usr/bin/env python3
# coding: utf-8

"""
=========================================================
  Scraper books / https://books.toscrape.com/index.html
=========================================================
"""
# import librairies
from time import sleep
from tqdm.auto import tqdm
from bs4 import BeautifulSoup


# import modules_p2
from utils.book_fetcher import BookFetcher
from utils.get_url_category import get_url_category
from utils.get_url_book import get_url_book
from utils.save_csv_book import save_csv_book
from utils.get_data import get_data
from utils.save_book_image import save_book_image


# specify the url
URL_INDEX = 'https://books.toscrape.com/index.html'


# get category url
def get_url(url_index: str) -> list:
    """[Find all urls for each category of books]

    Args:
        url_index (str): [url of the main book.toscrap page]

    Returns:
        list: [a list with the urls of each category]
    """
    url_ = get_url_category(url_index)
    return url_


# get next page url
def get_next_page(soup: BeautifulSoup, url: str) -> str:
    """[find the next page of a book category if there is one]

    Args:
        soup (BeautifulSoup): [A data structure representing a parsed HTML or XML document]
        url (str): [url of a book category]

    Returns:
        str: [The next page of a book category if there is one]
    """
    url = url.replace(url.split('/')[-1], '')
    if soup.find('ul', class_='pager'):
        page = soup.find('ul', class_='pager')
        if page.find('li', class_='next'):
            url = url + \
                str(page.find('li', class_='next').find('a')['href'])
            return url
        return None
    return None


# get page url
def get_all_page(url: str) -> list:
    """[Find all urls of books in a category]

    Args:
        url (str): [url of a book category]

    Returns:
        list: [A list of book urls]
    """
    url_book = get_url_book(url)
    return url_book


# get book
def get_all_book(url_book: list, rows: list):
    """[From a list of book urls, it finds all the information and adds them to rows]

    Args:
        url_book (list): [A list of book urls]
        rows (list) : [A list of data:
        product_page_url,
        upc,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        reviews_rating,
        image_url,
        filename]
    """
    # loop from book url
    for url in url_book:
        soup = get_data(url)
        # instence class BookFetcher
        book_info = BookFetcher(url, soup)
        book = book_info.get_book_info
        # write each result to rows
        rows.append(book)


# get book url
def srap_books(url: str, rows: list):
    """[From a book category url, call url_book (), get_all_book () and get_next_page ()]

    Args:
        url (str): [url of a book category]
        rows (list) : [A list of data:
        product_page_url,
        upc,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        reviews_rating,
        image_url,
        filename]
    """
    url_book = get_all_page(url)
    get_all_book(url_book, rows)
    # loop to get the next pages
    while True:
        soup = get_data(url)
        url = get_next_page(soup, url)
        if not url:
            break
        url_book = get_all_page(url)
        get_all_book(url_book, rows)
    del url_book[:]


def main(url):
    """
    Main instructions to run
    """
    print('========================================================')
    print('##### RUN SCRIPT.PY / P2_DA_PYTHON_OPENCLASSROOMS #####')
    print('========================================================')
    print('RUNNING...')
    # loop from second category url
    for i in tqdm(range(1, len(url))):
        rows = []
        srap_books(url[i], rows)
        # create csv and write rows list
        save_csv_book(rows)
        save_book_image(rows)
        # progress bar
        sleep(0.01)
        # cancel list
        del rows[:]
    print('##### END #####')


if __name__ == '__main__':
    URL = get_url(URL_INDEX)
    main(URL)
