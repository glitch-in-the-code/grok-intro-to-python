expense = input("Enter the expenses: ")
expense_split = expense.split()
total = 0

for expense in expense_split:
  total = total + int(expense)
  
print("Total: $" + str(total))

