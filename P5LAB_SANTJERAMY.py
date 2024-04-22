#AMY SANTJER
#04/10/2024
#P5LAB
#This program calculates and prints out a receipt for users

#calculate change     
def disperse_change(change):        
    #Get amount of change owed from the user
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed
    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")
    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")
    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")
    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")

#show list of availible items to checkout
def show_avail_items(dictionary):
    print(f"{'Grocery Item':<25}{'Price'}")
    print("-------------------------------")
    for key, value in dictionary.items():
        print(f"{key:<25}${value:.2f}")
    print("-------------------------------")

#adding grocery items to cart 
def add_items(dictionary):
    print("\n*Welcome to the Grocery Checkout*\n")
    itemEntered = str(input("Enter an item to add to the cart or type 'end' to stop adding items: "))
    itemsInCart = []
    while itemEntered != "end":
        if itemEntered in dictionary.keys():
            itemsInCart.append(itemEntered)
        else:
            print(f"The item {itemEntered} is not in stock!\n")
        itemEntered = str(input("Enter an item to add to the cart or type 'end' to stop adding items: "))
    return itemsInCart
 
#displays all items in the cart.
def show_cart(x, y):
    print("\nThe items currently in your cart are:")
    for x in y:
        print(x)

#calculating subtotal, tax, and total
def calc_total(itemsInCart, dictionary):
    print("\n*Grocery Checkout Receipt*")
    print("-------------------------------")
    total = 0
    for itemEntered in itemsInCart:
        total += dictionary[itemEntered]
        print(f"{itemEntered:<20}${dictionary[itemEntered]:.2f}")
    #Displays total
    print(f"\n{'SUBTOTAL:':<20}${total:.2f}\n")
    tax = total * .02 #2% tax
    finalTotal = tax + total 
    print(f"{'TAX:':<20}${tax:.2f}")
    print(f"{'TOTAL:':<20}${finalTotal:.2f}")
    return finalTotal

#Main function 
def main():
    items = {"apples": 3.69, "berries": 4.00, "chocolate": 2.89, "turkey": 6.99, "cheese": 4.00, "pepsi": 7.89, "eggs": 3.50, "bread": 3.00}
    show_avail_items(items)
    itemsInCart = add_items(items)
    show_cart(items, itemsInCart)
    finalTotal = calc_total(itemsInCart, items)
    print(f"\nYou owe ${finalTotal:.2f} for the groceries")
    cashInput = float(input("How much cash will you put in the self-checkout machine: $"))
    changeOwed = cashInput - finalTotal
    print(f"\nThe change owed to you is ${changeOwed:.2f}\n")
    changeOwed = round(changeOwed * 100)
    print(f"Dispensing...\n")
    disperse_change(changeOwed)

#Call the main function
main()




