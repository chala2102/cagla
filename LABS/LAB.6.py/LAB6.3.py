
expense_records = []
category_totals = {}
unique_categories = set()

print("=== PERSONAL EXPENSE TRACKER ===")

for i in range(1, 6):

    category = input(f"\nEnter expense {i} category: ")

    amount = float(input(f"Enter expense {i} amount: "))

    date = input(f"Enter expense {i} date (YYYY-MM-DD): ")

    expense_records.append((category, amount, date))


# Categorize
for category, amount, date in expense_records:

    unique_categories.add(category)

    category_totals[category] = category_totals.get(category, 0) + amount

all_amounts = [amount for category, amount, date in expense_records]

total_spending = sum(all_amounts)

average_expense = total_spending / len(all_amounts)

highest_expense_record = max(expense_records, key=lambda x: x[1])

lowest_expense_record = min(expense_records, key=lambda x: x[1])


print("\n=== OVERALL SPENDING SUMMARY ===")

print(f"Total Spending: ${total_spending:.2f}")

print(f"Average Expense: ${average_expense:.2f}")

print(f"Highest Expense: ${highest_expense_record[1]:.2f} "
      f"(Category: {highest_expense_record[0]}, Date: {highest_expense_record[2]})")

print(f"Lowest Expense: ${lowest_expense_record[1]:.2f} "
      f"(Category: {lowest_expense_record[0]}, Date: {lowest_expense_record[2]})")


print("\n=== UNIQUE CATEGORIES SPENT ON ===")

print(unique_categories)

print(f"Total unique categories: {len(unique_categories)}")


print("\n=== SPENDING BY CATEGORY ===")

for category, total in category_totals.items():

    print(f"{category}: ${total:.2f}")