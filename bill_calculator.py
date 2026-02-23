# Input from the user about his total income, food price, bill price, subscriptions, additional fees, anbd it will calculate money for saving or spending.


total_income = float(input("Enter your total income for this month: "))
rent = float(input("Enter your total rent cost for this month: "))
bills = float(input("Enter your total bills cost for this month - water heating electricity all of it: "))
subscriptions = float(input("Enter your total subscription cost for this month: "))
other_fees = float(input("Enter your total other fees combined cost for this month: " ))
savings = float(input("Enter the amount of cash you would like to set aside to save: "))

left_amount = total_income - (rent + bills + subscriptions + other_fees + savings)
print(f"You are left with {left_amount} at the end of the month")

input("Press Enter to exit...")
