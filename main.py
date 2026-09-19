from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

product1 = Product("Laptop", 800, 5)
product2 = Product("Mouse", 20, 10)
product3 = Product("Keyboard", 50, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Products:")
manager.display_all_products()

print("\nTotal inventory value:", manager.total_inventory_value())

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