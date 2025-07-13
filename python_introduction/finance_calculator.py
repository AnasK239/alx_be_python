

mon_income = int(input("Enter your monthly income: "))

mon_expenses = int(input("Enter your monthly expenses: "))

mon_savings = mon_income - mon_expenses
print(f"Your monthly savings are ${mon_savings}")


proj_savings = mon_savings*12 + (mon_savings*12 * 0.05)

print(f"Projected savings after one year, with interest, is: {proj_savings}")