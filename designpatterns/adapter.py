from abc import ABC, abstractmethod

class Pizza(ABC):
  @abstractmethod
  def toppings(self):
    pass

  @abstractmethod
  def bun(self):
    pass


class ChittagongPizza:
  def ctg_toppings(self):
    print("Chittagong style toppings")

  def ctg_bun(self):
    print("Chittagong style bun")


class DhakaPizza:
  def dhk_toppings(self):
    print("Dhaka style toppings")

  def dhk_bun(self):
    print("Dhaka style bun")


class ChittagongPizzaAdapter(Pizza, ChittagongPizza):
  def toppings(self):
    self.ctg_toppings()

  def buns(self):
    self.ctg_bun()


class DhakaPizzaAdapter(Pizza, DhakaPizza):
  def toppings(self):
    self.dhk_toppings()

  def bun(self):
    self.dhk_bun()