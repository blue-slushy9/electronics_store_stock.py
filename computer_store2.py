# Made this copy of the original program file for experimentation!

# Create a dictionary of products for sale at an electronics store, how 
# many of that item the store has in stock, and the price for each item; 
# please note that the prices are in dollars but I had to omit the $ signs;

electronics = {
        
        "laptop": {"Quantity": 100, "Price": 300},
        
        "desktop": {"Quantity": 50, "Price": 500},
        
        "router": {"Quantity": 30, "Price": 200},
        
        "switch": {"Quantity": 20, "Price": 100},
        
        "monitor": {"Quantity": 20, "Price": 75},
        
        "mouse": {"Quantity": 20, "Price": 10},
        
        "hard drive": {"Quantity": 25, "Price": 100}

}

# Prompts the user for their desired product and returns the input
def enter_product():
    product = input("Please enter the name of the product you would like "
                    "to buy now: ")
    # Throughout this program, print() is sometimes used to enhance legibility
    print()
    return product

# Creates a list of all of the electronics carried by the store, and then 
# joins them into string format, with each product separated by a comma
def print_electronics():

    # Create a list for all of our electronics
    electronics_list = []
    
    # electronics is the dictionary, this iterates over its keys
    for item in electronics:
        electronics_list.append(item)
    
    joined_electronics = (', '.join(electronics_list))
    # Now we inform the customer of what they can buy at this "store"
    print(joined_electronics)
    print()

# Prompt customer again after listing products that are in stock
def purchase_above_products(product):

    above_prods = input("Would you like to purchase one of the above\n"
                        "products? [Y/n]\n")
    # Use lower() to standardize user input, see below
    above_prods = above_prods.lower()

    if above_prods == 'y':
        #product = enter_product()
        # Go back to beginning of program
        beginning()
    elif above_prods == 'n':
        print(f"All right, no problem! Hopefully you can find {product}s\n"
                "at a different electronics store!\n")
        exit()
    else:
        print("Sorry, I didn't understand that. Why don't we start over?\n")
        beginning()

# If product is in our dictionary, then we check whether it is in stock
def is_in_stock(product):
    
    #if product in electronics: 
        
    # Define variable that will store current quantity of the product
    prod_quant = electronics[product]['Quantity']

    # Define variable that will store the price of the product
    prod_price = electronics[product]['Price']

    # The below should maybe be its own function? 4/4/24

    # Check the value in the dictionary, which is the number of that 
    # product that the store has in stock
    if prod_quant > 0:
        #print(f"We do have {product}s! How many would you like?\n")
        
        # Takes user input and casts it as an integer
        user_quant = input(f"We do have {product}s! We currently have "
                           f"{prod_quant} in stock. How many would you like? ")
        # Just to make output more legible
        print()
        # Cast user_quant as integer so we can perform calculations with it
        user_quant = int(user_quant)

    # We can maybe just embed this in the if statements below    
    # Calculate price total
    #total = (user_quant * prod_price)

    if user_quant <= prod_quant:
        total = (user_quant * prod_price)
        print(f"Great! That will be ${total}!")
        
    
    elif user_quant > prod_quant:
        buy_max_amount = input("I'm sorry, like I said we only have "
                              f"{prod_quant} {product}s in stock, would you "
                               "like to buy that amount instead? [Y/n]\n")
        
        if buy_max_amount == 'y':
            # Update user's desired quantity to quantity currently in stock
            user_quant = prod_quant             
            print(f"Great! That will be ${total}.\n")
            
            # These lines might need to go in a separate functions, and run at
            # a later time
            #new_prod_quant = (prod_quant - user_quant)
            #print(f"This is how many {product}s we have left after "
                   #f"the sale: {new_prod_quant}\n")
            

        elif buy_max_amount == 'n':
            print("OK, no problem. Would you like to hear again what " 
                  "products we have for sale? [Y/n]\n")

            hear_again = input().lower()
            print()

            if hear_again == 'y':
                print_electronics()
                product = enter_product()
            
            elif hear_again == 'n':
                print("OK, no problem! Hopefully you can find what you're "
                      "looking for at a different store.\n")
                    
    
    #print(f"This is how many {product}s we have left after the sale:")
    #print()
    #print(new_prod_quant)

# In the case that the product entered by the user is not in the inventory;
#else:

# Call this function only after making a sale to update dictionary/inventory
def update_stock(prod_quant, user_quant, product):
    # New product quantity in stock after selling some of them to user
    new_prod_quant = (prod_quant - user_quant)
    # Update dictionary to reflect new quantity in stock
    electronics[product]["Quantity"] = new_prod_quant

# The below may not need to be a function, however I will keep it for now 
# because I can't remember what I had in mind last year lol...

# You can encapsulate your entire program, or portions of it, inside of a
# function definition in order to restart the program as needed
def beginning():
    # sys.exit() terminates the program, exit status code is optional
    from sys import exit

    # Ask the customer what product they want, how many, give them the total 
    # for their order, and then update the inventory

    # I sometimes use print() statements to enhance legibility in the terminal
    print()

    # Call function that asks customer what product they want, capture output
    product = enter_product()

    if product not in electronics:
        print(f"Sorry, we don't carry {product}s at this time. These are the "
               "products we do carry:\n")
        # Print the electronics we have in stock, the current stock is dynamic
        print_electronics()
        # Prompt the user whether they want to purchase something now
        purchase_above_products(product)
    
    elif product in electronics:
        is_in_stock(product)
    # For legibility
    print()

# Verifies whether product is currently in stock
#is_in_stock(product)

# This is the first functional call that initiates the program
beginning()
