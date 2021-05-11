""" contains save_book_image function """
# import librairies
import urllib.request
import os


def save_book_image(books):
    """[summary]

    Args:
        books ([type]): [description]
    """
    dir_path = f'data/{books[0].category.replace(" ", "_").lower()}/images'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    for book in books:
        filename = book.filename
        file_path = os.path.join(dir_path, filename)
        urllib.request.urlretrieve(book.image_url, file_path)
        