from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

product1 = Product("Laptop", 900, 3)
product2 = Product("Mouse", 25, 15)
product3 = Product("Keyboard", 60, 5)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)



cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print("\nCart:")
cart.display_cart()

print("\nTotal cart value:", cart.total_cart_value())

print("\nAfter removing Mouse:")
manager.remove_product("Mouse")
manager.display_all_products()