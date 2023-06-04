#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = 0
  
  def add_item(self, title, price, quantity = 1):
    self.last_item = price * quantity
    if quantity > 1:
      self.total += price * quantity
      for each in range(quantity):
        self.items.append(title)
    else:
      self.total += price
      self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.discount / 100) * self.total
      print(f"After the discount, the total comes to ${int(self.total)}.")

    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_item