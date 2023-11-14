#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount= 0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.updated_items = []

    def __repr__(self):
      print(f'CashRegister(discount= {self.discount}, items= {self.items}, total= {self.total})')

    def add_item(self, item, price, quantity= 1):
      self.total += price * quantity
      for thing in range(quantity):
        self.items.append(item)
      self.updated_items.append({"item":item, "price":price, "quantity":quantity})

    def apply_discount(self):
      self.total = int(self.total * ((100 - self.discount)/ 100))
      if self.total > 0:
        print(f'After the discount, the total comes to ${self.total}.')
      else:
        print("There is no discount to apply.")
        
    def void_last_transaction(self):
      self.total -= self.updated_items[-1]["price"] * self.updated_items[-1]["quantity"]
