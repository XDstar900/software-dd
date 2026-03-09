
global wallet
wallet = 500
items = { # dictionary of items in the shop and their prices. Structure is item: (price, input number for user to select the item)
    "⚔️":(25,1),
    "🥽":(15,2),
    "🛡️":(30,3),
}
def shop():
    print(f"Welcome to the shop!\nYou have {wallet} points to spend.\nPlease type the number in the brackets next to the item you want to purchase:")
    for item, (price, input_number) in items.items(): #Loops though items in the shop and displays them in a readable format, with the price and the item.
        print(f"{item}: {price} points ({input_number})")
    
shop() 