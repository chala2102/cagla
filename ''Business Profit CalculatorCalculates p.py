print("=== Business Calculator ===")
revenue = float(input("whats the total revenue"))
expences = float(input("WHAT IS THE TOTAL EXPENCE"))
profit = revenue-expences
if profit > 0:
    print("WOAAAA YOU ARE DOING GREAT")
else:
    print("YOU SUCK  ;/")

margin = (profit / revenue) * 100
print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:,.2f}")
print(f"expences: ${expences:,.2f}")
print(f"profit: ${profit:,.2f}")






