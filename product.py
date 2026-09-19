class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def update_quantity(self, quantity):
        self.quantity = quantity