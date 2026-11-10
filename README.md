# Simple-Cafe-ordering-system

A command-line cafe ordering system written in Python. Customers can browse menus, build an order with quantities, remove items, and confirm their order with a running total in GBP.

Features
Three menu categories: Mains (16 items), Drinks (15 items) and Snacks & Desserts (30 items), 61 items in total
Quantity handling: choose any number of each item in a single step
Order editing: remove one item at a time from the order
Order summary: items grouped with quantities, line totals and an overall total
Order confirmation: confirm or cancel before the order is placed
Input validation: invalid menu choices, item numbers and quantities are caught and the user is asked again instead of the program crashing
How it works
Menus are stored as Python dictionaries mapping item names to prices
The order is stored as a list of (category, item, price) tuples
Each feature is its own function (display_menu, add_item_with_quantity, remove_item, show_order_summary, finalize_order), and a main loop (order_system) ties them together
Getting started

Requires Python 3. No external libraries are needed.

bash
python CafeProject_Final.py

Then follow the on-screen menu:

View and order mains
View and order drinks
View and order snacks and desserts
Remove an item from your order
View your order summary
Confirm your order
Exit
What I learned
Structuring a program into small, reusable functions
Using dictionaries, lists and tuples to store and process data
Validating user input to make a program more reliable
Building a menu-driven loop for a command-line application
Possible improvements
Save orders to a file
Add a search or filter for menu items
Add a graphical interface
