"""contains get_book function"""

# import librairies
from urllib.parse import urljoin

# import utils
from utils.get_data import get_data

# import models
from models.book import Book


class BookFetcher:
    """[Class BookFetcher]
    """
    def __init__(self, url, soup):
        self.url = url
        self.soup = soup

    def get_upc(self):
        """return upc"""
        try:
            upc = self.soup.select_one("table > tr > td").text
            return upc
        except Exception as err:
            print("OOps: the upc of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_title(self):
        """return title"""
        try:
            title = self.soup.select_one("h1").text.replace('/', '_')
            return title
        except Exception as err:
            print("OOps: the title of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_price_including_tax(self):
        """return price_including_tax"""
        try:
            price_including_tax = self.soup.select(
                "table > tr")[3].select_one("td").text
            return price_including_tax
        except Exception as err:
            print("OOps: the price including tax of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_price_excluding_tax(self):
        """return price_excluding_tax"""
        try:
            price_excluding_tax = self.soup.select(
                "table > tr")[2].select_one("td").text
            return price_excluding_tax
        except Exception as err:
            print("OOps: the price excluding tax of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_number_available(self):
        """return number_available"""
        try:
            number_available = self.soup.select("table > tr")[
                5].select_one("td").text
            number_available = number_available.replace(
                'In stock (', '').replace(' available)', '')
            return number_available
        except Exception as err:
            print("OOps: the number available of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_product_description(self):
        """return product_description"""
        try:
            product_description = self.soup.select_one(".sub-header + p").text
            return product_description
        except Exception as err:
            print("OOps: the description of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_category(self):
        """return category"""
        try:
            category = self.soup.select(".breadcrumb > li")[
                2].select_one("a").text
            return category
        except Exception as err:
            print("OOps: the category of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_reviews_rating(self):
        """return reviews rating"""
        try:
            reviews_rating = self.soup.select(
                "table > tr")[6].select_one("td").text
            return reviews_rating
        except Exception as err:
            print("OOps: the reviews rating of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_image_url(self):
        """return image_url"""
        try:
            image_source = self.soup.select_one(".item > img")["src"]
            image_url = urljoin('http://books.toscrape.com/', image_source)
            return image_url
        except Exception as err:
            print("OOps: the image url of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_filename(self):
        """return filename"""
        try:
            image_file = self.get_title().replace(" ", "_").lower()
            filename = image_file + '.jpg'
            return filename
        except Exception as err:
            print("OOps: the filename of the book", self.get_title(), "of the category",
                  self.get_category(), "does not exist.", "ERROR:", err)
            return

    def get_book_info(self):
        """return book_info"""
        book_info = Book(
            self.url,
            self.get_upc(),
            self.get_title(),
            self.get_price_including_tax(),
            self.get_price_excluding_tax(),
            self.get_number_available(),
            self.get_product_description(),
            self.get_category(),
            self.get_reviews_rating(),
            self.get_image_url(),
            self.get_filename()
        )
        return book_info
