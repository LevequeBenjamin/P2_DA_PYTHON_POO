class Book:
    def __init__(self,
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
                 filename
                 ):
        self.product_page_url = product_page_url
        self.upc = upc
        self.title = title
        self.price_including_tax = price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.reviews_rating = reviews
        self.image_url = image_url
        self.filename = filename

