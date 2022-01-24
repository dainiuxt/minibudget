from modules.record import (Incomes as Plus,
                            Expenses as Minus)
from modules.budget import Budget

#Create initial dataset
mybudget = Budget()

mybudget.append(Plus(1200, "alga"))
mybudget.append(Minus(300, "paltas"))
mybudget.append(Plus(150, "avansas"))
mybudget.append(Minus(25, "kinas"))

while True:
  main_menu = int(input("1: enter incomes\n2: enter expenses\n3: read data\n0: exit program\n"))
  if main_menu == 1:
    income_qty = float(input("Enter income sum (use '.' for decimal): "))
    income_source = input("Enter income source: ")
    mybudget.append(Plus(income_qty, income_source))
  elif main_menu == 2:
    expense_qty = float(input("Enter income sum (use '.' for decimal): "))
    if float(mybudget.total()) - expense_qty < 0:
        print('You don\'t have credit line!')
    else:
        expense_source = input("Enter income source: ")
        mybudget.append(Plus(expense_qty, expense_source))
  elif main_menu == 3:
    while True:    
        print('1: incomes list')
        print('2: incomes total')
        print('3: expenses list')
        print('4: expenses totals')
        print('5: total ballance')
        print('0: go back')
        list_menu = int(input())
        if list_menu == 1:
            mybudget.listinc()
        elif list_menu == 2:
            mybudget.suminc()
        elif list_menu == 3:
            mybudget.listexp()
        elif list_menu == 4:
            mybudget.sumexp()
        elif list_menu == 5:
            mybudget.listall()
            mybudget.total()
        elif list_menu == 0:
            break
        continue
  if main_menu == 0:
    print('Quit')
    break
