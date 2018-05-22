from .item import Item

class Pricer:
  def __init__(self, price_map):
    self.price_map = price_map

  def price(self, basket):
    return [Item(name, self.price_map[name]) for name in basket]
