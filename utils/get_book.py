"""contains get_book function"""

# import librairies
import urllib.request
from urllib.parse import urljoin
from slugify import slugify


# import modules_p2
from utils.get_data import get_data
from utils.save_csv_book import save_csv_book


class Book:
    """[Class Book]
    """

    def get_upc(self, soup):
        try:
            upc = soup.select_one("table > tr > td").text
            return upc
        except:
            return

    def get_title(self, soup):
        try:
            title = soup.select_one("h1").text.replace('/', '_')
            return title
        except:
            return

    def get_price_including_tax(self, soup):
        try:
            price_including_tax = soup.select(
                "table > tr")[3].select_one("td").text
            return price_including_tax
        except:
            return

    def get_price_excluding_tax(self, soup):
        try:
            price_excluding_tax = soup.select(
                "table > tr")[2].select_one("td").text
            return price_excluding_tax
        except:
            return

    def get_number_available(self, soup):
        try:
            number_available = soup.select("table > tr")[
                5].select_one("td").text
            number_available = number_available.replace(
                'In stock (', '').replace(' available)', '')
            return number_available
        except:
            return

    def get_product_description(self, soup):
        try:
            product_page_url = soup.select_one(".sub-header + p").text
            return product_page_url
        except:
            return

    def get_category(self, soup):
        try:
            category = soup.select(".breadcrumb > li")[2].select_one("a").text
            return category
        except:
            return

    def get_reviews_rating(self, soup):
        try:
            reviews_rating = soup.select("table > tr")[6].select_one("td").text
            return reviews_rating
        except:
            return

    def get_image_url(self, soup):
        try:
            image_source = soup.select_one(".item > img")["src"]
            image_url = urljoin('http://books.toscrape.com/', image_source)
            return image_url
        except:
            return

    def get_filename(self, soup):
        try:
            product_page_url = url
            return product_page_url
        except:
            return

    def get_book_info(self, url):
        try:
            soup = get_data(url)
            book_info = [
                url,
                self.get_upc(soup),
                self.get_title(soup),
                self.get_price_including_tax(soup),
                self.get_price_excluding_tax(soup),
                self.get_number_available(soup),
                self.get_product_description(soup),
                self.get_category(soup),
                self.get_reviews_rating(soup),
                self.get_image_url(soup),
            ]
            return book_info
        except:
            print("Error")
