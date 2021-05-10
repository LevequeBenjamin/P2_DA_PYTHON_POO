from utils.get_book import Book
from utils.save_csv_book import save_csv_book
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
book = Book()
book_info = book.get_book_info(url)
save_csv_book(book_info)
print(book_info)