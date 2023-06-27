# Create a dictionary of products for sale at an electronics store, how many
# of that item the store has in stock, and the price for each item; please
# note that the prices are in dollars but I had to omit the $ signs;

electronics = {
        
        "laptop": {"Quantity": 100, "Price": 500},
        
        "desktop": {"Quantity": 50, "Price": 500},
        
        "router": {"Quantity": 30, "Price": 100},
        
        "switch": {"Quantity": 20, "Price": 50},
        
        "monitor": {"Quantity": 20, "Price": 75},
        
        "mouse": {"Quantity": 20, "Price": 25},
        
        "hard drive": {"Quantity": 25, "Price": 250}

}

# Ask the customer what product they want, how many, give them the total for 
# their order, and then update the inventory;

# Throughout this program, I use many print() statements to enhance legibility
# in the terminal, e.g. below;
print()

print("Please enter the name of the product you would like to buy now...")
print()
product = input()
print()

if product in electronics: 
    
    # Check the value in the dictionary, which is the number of that product
    # that the store has in stock;
    if electronics[product]['Quantity'] > 0:
        print(f"We do have {product}s! How many would you like?")
        print()
        quantity = int(input())
        print()

    if quantity == 1:
        print(f"Great! We do have 1 {product} available. That will be {electronics[product]['price']}.")
    
    elif quantity <= electronics[product]['Quantity']:
        total = (quantity * electronics[product]['Price'])
        print(f"Great! We do have {quantity} {product}s available. That will be ${total}!")
        print()
    
    elif quantity > electronics[product]['Quantity']:
        print(f"I'm sorry, we only have {electronics[product]['Quantity']}\n"
                f"{product}s in stock, would you like to buy that amount\n" 
                "instead?")
        print()

        buy_lower_amount = input().lower()

    electronics[product]['Quantity'] = (electronics[product]['Quantity'] - quantity)

    print(f"This is how many {product}s we have left after the sale:")
    print()
    print(electronics[product]['Quantity'])

# In the case that the product entered by the user is not in the inventory;
else:
    print(f"Sorry, we don't carry {product}s at this time.")
print()

