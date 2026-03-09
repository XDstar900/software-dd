
global wallet
wallet = 500
items = { # dictionary of items in the shop and their prices. Structure is item: (price, input number for user to select the item)
    "⚔️":(25,1),
    "🥽":(15,2),
    "🛡️":(30,3),
}
def shop():
    print(f"Welcome to the shop!\nYou have {wallet} points to spend.\n Please choose one of the following options:\nBuy\t(A)\nView owned items\n Leave")
    for item, (price, input_number) in items.items(): #Loops though items in the shop and displays them in a readable format, with the price and the item.
        print(f"{item}: {price} points ({input_number})")
        Purchase = input("Please inpu ")
    
shop() 