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
    id=0 #class variable

    def __init__(self, description, list_price):
        self.id = self.generate_product_id()
        super().__init__(description, list_price)


    def generate_product_id(cls):
        """
        Update class ID
        """
        cls.id += 1
        return "VG" + f"{cls.id:06}"





