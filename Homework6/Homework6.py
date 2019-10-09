# ----------------------------------------------------------------------
# Name:     Homework 6
# Purpose:  Implement a product database
#
# Author:   Ian SooHoo
# ----------------------------------------------------------------------
""" Product Database

User enters products that they want to keep track of including reviews,
descriptions, and sales. Products can be bundled together and stock
is kept track of.
"""

class Product:
    """
    Represent a product

    Arguments:
    description (string): product description
    list_price (int): product price

    Attributes:
    id (int): the product id
    """
    id = 0  # class variable

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.id = self.generate_product_id()
        # print("THE ID IS: "+ self.id)
        self.sales = []
        self.reviews = []


    def restock(self, quantity):
        """
                Add quantity to the stock.
                :param quantity: (number) amount of quantity to add.
                return: nothing
        """
        self.stock += quantity

    def review(self, stars, text):
        """
                Keep track of reviews.
                :param stars: (number) amount of stars a review has.
                :param text:(string) the text of the review
                """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
                Keep track of sold items.
                :param quantity: (number) amount of quantity that was sold.
                :param sale_price: (number) dollar amount at which item was
                sold.
                return: nothing
                """
        for i in range(quantity):
            if self.stock > 0:  # if there is something in stock
                self.sales.append(sale_price)
                self.stock -= 1

    @classmethod
    def generate_product_id(cls):

        """
               Update class ID
               return: (string) an id number for each individual product with
               appropriate prefix
               """
        cls.id += 1
        return "GN" + f"{cls.id:06}"

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.id}\nList price: $' \
               f'{self.list_price:.2f}\nAvailable in stock: {self.stock}'

    def __add__(self, other):
        return Bundle(self,other)

    @property
    def lowest_price(self):
        """
               Generates the lowest price
                """
        if len(self.sales) > 0:
            return min(self.sales)
        else:
            return None

    @property
    def average_rating(self):
        """
                Finds the average rating
                """
        if len(self.reviews) > 0:
            return sum(review[1] for review in self.reviews) / len(
                self.reviews)
        else:
            return None


class VideoGame(Product):
    """
    Video Game product
    Argument:
    description
    list_price
    Attributes:
    id

    Inherits from Product
    """
    id = 0

    def __init__(self, description, list_price):
        super().__init__(description, list_price)

    @classmethod
    def generate_product_id(cls):
        """
                Update class ID
                return: (string) an id number for each individual product with
                appropriate prefix

                """

        cls.id += 1
        print(cls.id)
        return f"VG{cls.id:06}"

class Book(Product):
    """
       Book product
       Argument:
       description
       list_price
       author
       pages
       Attributes:
       id

       Inherits from Product
       """
    id = 0

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
        return: (string) an id number for each individual product with
        appropriate prefix
        """
        cls.id += 1
        # print(cls.id)
        return f"BK{cls.id:06}"

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __ge__(self, other):
        return self.pages >= other.pages


class Bundle(Product):
    """
          Bundle of products
           Argument:
           2 required products and as many other products beyond that
           Attributes:
           id
           bundle_discount - decimal of discount

           Inherits from Product
           """
    bundle_discount = .20
    id = 0

    def __init__(self, req1, req2, *args):
        self.description = f'{req1.description} & {req2.description}'

        for arg in args:
            self.description = self.description + " & " + arg.description

        self.list_price = (1 - Bundle.bundle_discount) * (req1.list_price +
                req2.list_price + sum(arg.list_price for arg in args))

        super().__init__(self.description, self.list_price)

    @classmethod
    def generate_product_id(cls):
        """
               Update class ID
               return: (string) an id number for each individual product with
               appropriate prefix
               """
        cls.id += 1
        # print(cls.id)
        return f"BL{cls.id:06}"
