from .record import (Incomes as Plus,
                    Expenses as Minus)

class Budget:
  def __init__(self):
    self.book = []

  def append(self, rec):
    self.book.append(rec)

  def listexp(self):
    print("Expenses:")
    for rec in self.book:
      if isinstance(rec, Minus):
        print(f"{rec.descr}: €{rec.qty}")

  def listinc(self):
    print("Incomes:")
    for rec in self.book:
      if isinstance(rec, Plus):
        print(f"{rec.descr}: €{rec.qty}")

  def suminc(self):
    self.incomes = float(0)
    for rec in self.book:
      if isinstance(rec, Plus):
        self.incomes += rec.qty
    print(f"Your total incomes are €{self.incomes}.")

  def sumexp(self):
    self.expenses = float(0)
    for rec in self.book:
      if isinstance(rec, Minus):
        self.expenses += rec.qty
    print(f"Your total expenses are €{self.expenses}.")

  def listall(self):
    print("All records:")
    for rec in self.book:
      if isinstance(rec, Minus):
        print(f"{rec.descr}: -€{rec.qty}")
      if isinstance(rec, Plus):
        print(f"{rec.descr}: €{rec.qty}")

  def total(self):
    self.incomes = float(0)
    self.expenses = float(0)
    for rec in self.book:
      if isinstance(rec, Plus):
        self.incomes += rec.qty
    for rec in self.book:
      if isinstance(rec, Minus):
        self.expenses += rec.qty
    totals = self.incomes - self.expenses
    print(f"Your ballance is €{totals}.")
    return totals
