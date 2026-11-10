# The order will be stored in this list, with items being added or removed
order = []

# Sample menu items for the three categories (in GBP)
mains = {
  'Full English Breakfast': 15.50,
  'Egg Benedict': 10.50,
  'Avocado On Sourdough': 7.50,
  'Vegetarian Full Breakfast': 7.50,
  'Gourmet Beef Burger': 14.50,
  'Chicken Tikka Masala': 8.75,
  'Classic Lasagne': 8.75,
  'Hand Battered Fish And Chips': 13.50,
  'Chicken Sandwich': 7.50,
  'Oats': 4.00,
  'Cajun Chicken Pasta': 13.95,
  'Loaded Jacket Potato': 6.50,
  'Turkey Ham And Cheese Omelette': 8.80,
  'Beef Burger': 8.50,
  'Chicken Alfredo': 8.65,
  'Plain Omelette': 5.00
}
 
drinks = {
  'Karak Chaii': 3.25,
  'Pink Tea (Kashmiri)': 3.90,
  'Mango Lassi': 4.50,
  'Rose Milkshake': 4.50,
  'Turkish Coffee': 3.50,
  'Fresh Mint Tea': 2.60,
  'Iced Saffron Latte': 4.50,
  'Strawberry Limbu Pani': 3.50,
  'Flat White': 4.35,
  'Americano': 3.80,
  'Belgian Hot Chocolate': 4.60,
  'Caffe Mocha': 4.60,
  'Rubicon Mango (Can)': 1.50,
  'Fresh Orange Juice': 3.50,
  'Virgin Mojito': 5.50
}
 
snacks_desserts = {
  'Chocolate Fudge Cake': 4.50,
  'Victoria Sponge': 4.00,
  'Carrot & Walnut Cake': 4.25,
  'Biscoff Cheesecake': 4.50,
  'Sticky Toffee Pudding': 5.50,
  'Lemon Drizzle Cake': 3.80,
  'Warm Apple Crumble': 5.00,
  'Belgian Waffles': 5.95,
  'Chocolate Brownie': 3.25,
  'Red Velvet Cake': 4.50,
  'Fruit Scone With Cream & Jam': 3.50,
  'Tiramisu Slice': 5.00,
  'Bakewell Slice': 3.95,
  'Stacked Pancakes': 4.50,
  'Macaron Selection (Pack Of 3)': 5.00,
  'Sausage Roll': 4.00,
  'Ham & Cheese Croissant': 4.70,
  'Pain Au Chocolat': 3.40,
  'Chocolate Chip Cookie': 2.85,
  'Blueberry Muffin': 3.30,
  'Salted Caramel Flapjack': 3.25,
  'Fruit Scone & Butter': 2.85,
  'Cinnamon Danish': 3.40,
  'Caramel Shortbread': 3.15,
  'Banana & Walnut Loaf Cake': 3.40,
  'Berry Granola Pot': 3.20,
  'BOSH! Pecan Slice (Vegan)': 3.25,
  'Hummus & Falafel Mezze Salad': 8.30,
  'Fruited Teacake': 2.75,
  'Almond Croissant': 3.20
}
# The order will be stored in this list, with items being added or removed
order = []
 
# Function to display the menus
def display_menu(menu, title):
    print(f"\n--- {title} ---")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item}: £{price:.2f}")
 
# Function to add an item with a quantity
def add_item_with_quantity(menu, category):
    display_menu(menu, category)
    item_choice = input("Select item number (or 0 to go back): ")
    items = list(menu.items())
    if item_choice.isdigit() and 1 <= int(item_choice) <= len(items):
        item, price = items[int(item_choice) - 1]
        qty = input(f"How many {item}s would you like? ")
        if qty.isdigit() and int(qty) > 0:
            for _ in range(int(qty)):
                order.append((category, item, price))
            print(f"{qty}x {item} added to your order.")
        else:
            print("Invalid quantity.")
    else:
        print("Invalid choice.")
 
# Function to remove an item from the order
def remove_item():
    if not order:
        print("Your order is empty.")
        return
    # Show current unique items with numbers
    counts = {}
    for category, item, price in order:
        if item in counts:
            counts[item][0] += 1
        else:
            counts[item] = [1, price]
    print("\n--- Remove Item ---")
    items_list = list(counts.items())
    for i, (item, (qty, price)) in enumerate(items_list, 1):
        print(f"{i}. {item} x{qty}: £{price * qty:.2f}")
    choice = input("Select item number to remove one of (or 0 to go back): ")
    if choice.isdigit() and 1 <= int(choice) <= len(items_list):
        item_to_remove = items_list[int(choice) - 1][0]
        for i, (category, item, price) in enumerate(order):
            if item == item_to_remove:
                del order[i]
                print(f"One {item_to_remove} removed from your order.")
                return
    else:
        print("Invalid choice.")
 
# Function to show the order summary with quantities and total cost
def show_order_summary():
    print("\n--- Your Order ---")
    if not order:
        print("Your order is empty.")
        return 0
    counts = {}
    for category, item, price in order:
        if item in counts:
            counts[item][0] += 1
        else:
            counts[item] = [1, price]
    total = 0
    for item, (qty, price) in counts.items():
        print(f"{item} x{qty}: £{price * qty:.2f}")
        total += price * qty
    print(f"\nTotal: £{total:.2f}")
    return total
 
# Function to finalise the order
def finalize_order():
    total = show_order_summary()
    if total > 0:
        confirm = input("\nConfirm order? (y/n): ").lower()
        if confirm == 'y':
            print("Thank you! Your order has been placed.")
        else:
            print("Order cancelled.")
    else:
        print("No items in order.")
 
# Main program logic to interact with the user
def order_system():
    while True:
        print("\nWelcome to FutureSkills Cafe")
        print("1. View & Order Mains")
        print("2. View & Order Drinks")
        print("3. View & Order Snacks & Desserts")
        print("4. Remove item from order")
        print("5. View order summary")
        print("6. Confirm order")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item_with_quantity(mains, 'Mains')
        elif choice == '2':
            add_item_with_quantity(drinks, 'Drinks')
        elif choice == '3':
            add_item_with_quantity(snacks_desserts, 'Snacks & Desserts')
        elif choice == '4':
            remove_item()
        elif choice == '5':
            show_order_summary()
        elif choice == '6':
            finalize_order()
            break
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
 
# Run the ordering system
order_system()
