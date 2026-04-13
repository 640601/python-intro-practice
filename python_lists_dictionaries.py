# ======================================
# PYTHON LISTS AND DICTIONARIES EXERCISE
# ======================================

print("\n" + "="*40)
print("PYTHON LISTS AND DICTIONARIES")
print("="*40)

# --------------------------------------
# PART 1: LIST OPERATIONS
# --------------------------------------

print("\n--- LIST OPERATIONS ---")

# Create a shopping list with at least 5 items
shopping_list = ["apple", "banana", "milk", "bread", "eggs"]

# Print the third item
print("Third item in the list:", shopping_list[2])

# Replace the first item
shopping_list[0] = "orange"
print("Updated list after replacing first item:", shopping_list)

# Add an item to the end
shopping_list.append("chicken")
print("List after adding a new item:", shopping_list)


# --------------------------------------
# PART 2: DICTIONARY OPERATIONS
# --------------------------------------

print("\n--- DICTIONARY OPERATIONS ---")

# Create a dictionary with 3 items and prices
grocery_prices = {
    "apple": 1.50,
    "milk": 2.00,
    "bread": 2.50
}

# Print one item and its price
print(f"The price of milk is ${grocery_prices['milk']}")

# Add a new item
grocery_prices["eggs"] = 3.00
print("Updated dictionary:", grocery_prices)

# Calculate total cost
total_cost = sum(grocery_prices.values())
print("Total cost of all items: $", total_cost)
