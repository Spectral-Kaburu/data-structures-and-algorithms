monthly_expenses = [2200, 2350, 2600, 2130, 2190]

monthly_expenses[2] = monthly_expenses[2] + 200
more = monthly_expenses[1] - monthly_expenses[0]
quarter = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
monthly_expenses.insert(5, 1980)

for i in monthly_expenses:
    if i == 2000:
        print(i)


print(more)
print(quarter)
