# Shopping List Program

def shopmart():
    inventory = ["apple", "banana", "soda", "chicken", "chips"]
    shopping_cart = []

    print("Hello! Welcome to Shopmart!")

    start = input("Would you like to do some shopping? (Y/N): ").upper()

    if start == "Y":
        while True:
            print("\nAvailable inventory:")
            for item in inventory:
                print("-", item)

            choice = input("\nSelect an item to add to your shopping cart: ").lower()

            if choice in inventory:
                if choice not in shopping_cart:
                    shopping_cart.append(choice)
                    print(f"{choice} successfully added to your cart!")
                else:
                    print("Item already in your cart.")
            else:
                print("Item not found in inventory.")

            continue_shopping = input("Would you like to continue shopping? (Y/N): ").upper()

            if continue_shopping == "N":
                break

        print("\nThank you for shopping at Shopmart!")
        print("Your shopping cart includes:", shopping_cart)

    else:
        print("Thank you! Have a great day!")


# Run the program
shopmart()