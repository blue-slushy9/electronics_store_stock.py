# Create a dictionary of products for sale at an electronics store, and how many the store has in stock

electronics = {"laptop":100,"desktop":50,"router":30,"switch":20,"monitor":20,"mouse":20,"hard drive":25}

# Ask the customer what product they want, how many, the total for their order, and then update the inventory

print("Please enter the name of the product you would like to buy now...")
product = input()

if product in electronics and electronics[product] > 0:
    print(f"We do have {product}s! How many would you like?")
    quantity = int(input())
    if quantity == 1:
        print(f"Great! We do have 1 {product} available. That will be $100.")
    elif quantity <= electronics[product]:
        total = (quantity * 100)
        print(f"Great! We do have {quantity} {product}s available. That will be ${total}!")
    electronics[product] = (electronics[product] - quantity)
print()

print(f"This is how many {product}s we have left after the sale:")
print(electronics[product])
