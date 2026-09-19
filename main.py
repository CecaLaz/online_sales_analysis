from product import Product
from product_manager import ProductManager


manager = ProductManager()

product1 = Product("Laptop", 900, 3)
product2 = Product("Mouse", 25, 15)
product3 = Product("Keyboard", 60, 5)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)



print("\nAfter removing Mouse:")
manager.remove_product("Mouse")
manager.display_all_products()