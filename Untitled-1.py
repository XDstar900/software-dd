
global wallet
wallet = 500
items = { # dictionary of items in the shop and their prices. Structure is item: (price, input number for user to select the item)
    "⚔️":(25,(1)),
    "🥽":(15,(2)),
    "🛡️":(30,(3)),
}
def shop():
    global wallet
    print(f"Welcome to the shop!\nYou have {wallet} points to spend.")
    while True: #Loop that keeps the shop running until the user chooses to leave.
        choice = input("Please choose one of the following options:\nBuy (A)\nView owned items (B)\nLeave (C)\nYour option: ").upper()
        match choice:
            case "A":
                for item, (price, input_number) in items.items(): #Loops though items in the shop and displays them in a readable format, with the price and the item.
                    print(f"{item}: {price} points ({input_number})")
                Purchase = input("Please input the number in brackets for the item you wish to purchase: ")
                #with purchase loop through itmes to find out price and the item the user wants to purchase. If they have enough points, they purchase the item and it is added to their owned items. If they do not have enough points, they are informed and looped back to the shop menu.
                for item, (price, input_number) in items.items():
                    if Purchase == input_number:
                        print(item)
                        print(price)
                        print(input_number)
                        if wallet >= price:
                            wallet -= price
                            Owned_items.append(item)
                            print(f"You have purchased {item} for {price} points. You have {wallet} points left.")
                        else:
                            print("You do not have enough points to purchase this item.")
            case "B":
                print(f"You own these items:")
                for item in Owned_items: #Loops through the items the user has purchased and displays them.
                    print(item)
            case "C":
                print("Thank you for visiting the shop!")
                return
            case _:
                print("Invalid option, please try again.")
    
shop() 