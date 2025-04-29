#Define the menu of restaurant
menu = {
    'pizza': 80,
    'pasta': 110,
    'burger': 70,
    'salad': 60,
    'coffee': 40,
    'water': 20,
}

# Greet
print("Welcome to Marry Restaurant!")
print("\nHere is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs {price}")

order_total = 0

# Taking first order
item_1 = input("\nEnter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

# Asking for another order
another_order = input("\nDo you want to add another item? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

print(f"\nThe total amount to pay is: Rs {order_total}")
