class Record:
  def __init__(self, qty):
    self.qty = qty

  def __str__(self):
      return f"{self.qty}"

class Incomes(Record):
    def __init__(self, qty, descr):
        super().__init__(qty)
        self.descr = descr

    def __repr__(self):
        return f"({self.qty}: {self.descr})"

class Expenses(Record):
    def __init__(self, qty, descr):
        super().__init__(qty)
        self.descr = descr

    def __repr__(self):
        return f"({self.qty}: {self.descr})"
        