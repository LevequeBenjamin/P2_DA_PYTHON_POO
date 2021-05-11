""" contains save_book_image function """
# import librairies
import urllib.request
import os


def save_book_image(books: list):
    """[Download images from books]

    Args:
        books (list): [
        A list of data:
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
        ]
    """
    dir_path = f'data/{books[0].category.replace(" ", "_").lower()}/images'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    for book in books:
        filename = book.filename
        file_path = os.path.join(dir_path, filename)
        urllib.request.urlretrieve(book.image_url, file_path)
