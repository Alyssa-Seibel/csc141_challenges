# Alyssa Seibel
# Date: 9/5/24
# Challenge #2 : Calculations of spendings with and without tax



PA_TAX = 0.06
PRICE_OF_MEAL = 12.49
tax = (PA_TAX*PRICE_OF_MEAL)
wo_tax = (PRICE_OF_MEAL*5)
tax_each_meal = ()
#w_tax = ([(PRICE_OF_MEAL*5)*PA_TAX]*5)
w_tax =((PRICE_OF_MEAL+tax)*5)



print()
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax Per Meal: {tax}")
print(f"Total Without Tax: {wo_tax}")
print(f"Total With Tax:{w_tax}")
print("-------------------------")
print()