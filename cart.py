"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:
  def __init__(self):
    self.cart = {}

  def add_items(self,item,price):
    self.cart[item] = price
    print(f"{item} added to the cart at price {price}")

  def remove_items(self,item):
    if item in self.cart:
      del self.cart[item]
      print(f"{item} remove succesfully")
    else:
      print(f"{item} not found in cart")

  def total_price(self):
    total = sum(self.cart.values())
    print(f"total price is {total}")
    return total
  def clear(self):
    self.cart.clear()
    print(f"empty cart")

cart = ShoppingCart()
cart.add_items("shirt",7000)
cart.add_items("laptop",100000)
cart.remove_items("shirt")
print(cart.add_items("phone",7000))
