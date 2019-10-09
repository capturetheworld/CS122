class Product:

    id = 0 #class variable


    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.id = self.generate_product_id()
        # print("THE ID IS: "+ self.id)
        self.sales = []
        self.reviews = []

    def restock(self,quantity):
        self.stock += quantity

    def review(self, stars, text):
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        for i in range(quantity):
            if self.stock > 0: #if there is something in stock
                self.sales.append(sale_price)
                self.stock -= 1

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
        """
        cls.id += 1
        return "GN" + f"{cls.id:06}"

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.id}\nList price: $' \
               f'{self.list_price:.2f}\nAvailable in stock: {self.stock}'

    @property
    def lowest_price(self):
        if len(self.sales) > 0:
            return min(self.sales)
        else:
            return None

    @property
    def average_rating(self):
        if len(self.reviews) > 0:
            return sum(review[1] for review in self.reviews)/len(self.reviews)
        else:
            return None

class VideoGame(Product):
    id = 0

    def __init__(self, description, list_price):
        super().__init__(description, list_price)

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
        """
        cls.id += 1
        # print(cls.id)
        return f"VG{cls.id:06}"

    class VideoGame(Product):
        id = 0

        def __init__(self, description, list_price):
            super().__init__(self,description, list_price)

        @classmethod
        def generate_product_id(cls):
            """
            Update class ID
            """
            cls.id += 1
            # print(cls.id)
            return f"VG{cls.id:06}"


class VideoGame(Product):
    id = 0

    def __init__(self, description, list_price):
        super().__init__(description, list_price)

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
        """
        cls.id += 1
        # print(cls.id)
        return f"VG{cls.id:06}"

class Book(Product):
    id = 0

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
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
    bundle_discount = .20
    id = 0

    def __init__(self, req1,req2, *args):
        self.description = "some bundle"
        self.list_price = (1-Bundle.bundle_discount)*(req1.list_price +
                                               req2.list_price+sum(
                    arg.list_price for arg in args))
        super().__init__(self.description, self.list_price)

    @classmethod
    def generate_product_id(cls):
        """
        Update class ID
        """
        cls.id += 1
        # print(cls.id)
        return f"BL{cls.id:06}"








