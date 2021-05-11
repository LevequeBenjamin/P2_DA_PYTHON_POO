"""contains save_csv_book function"""
# import libraries
import csv
import os
from pathlib import Path


# Create csv and write rows to output file
def save_csv_book(books):
    """[Create a csv file, and write all the data found from each book]

    Args:
        rows (list): [A list of data:
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
    #extract category from the name
    dir_path = f'data/{books[0].category.replace(" ", "_").lower()}'
    filename = f'{books[0].category.replace(" ", "_").lower()}.csv'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, filename)
    with open(f'{file_path}', 'w', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        if Path(f"{file_path}").stat().st_size == 0:
            # create and write headers to a list
            writer.writerow([
                "product_page_url",
                "universal_product_code(upc)",
                "title", "price_including_tax",
                "price_excluding_tax",
                "number_available",
                "product_description",
                "categorie",
                "review_rating",
                "image_url",
                "filename"
            ])
        for book in books:
            # create and write rows list
            writer.writerow([
                book.product_page_url,
                book.upc,
                book.title,
                book.price_including_tax,
                book.price_including_tax,
                book.number_available,
                book.product_description,
                book.category,
                book.reviews_rating,
                book.image_url,
                book.filename
            ])
