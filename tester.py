from tkinter import * # for UI
from random import choice # question choosing
from colorama import *  # for coloured text
from time import sleep # for delays after answering questions 

UI = Tk()
User = Entry()
Password = Entry()
attempts = 3
global Wallet # allows user's point wallet to be modified by any function
Wallet = 0
init(autoreset=True) 
Owned_items = [] #List of items the user has purchased.
items = { # dictionary of items in the shop and their prices. Structure is item: (price, input number for user to select the item)
    "⚔️ ":(25,("1")),
    "🥽 ":(15,("2")),
    "🛡️ ":(30,("3")),
    "🧀 ":(20,("4"))
}  

# Logic for creditiential validation. Occurs when button in pressed. 
def login():
    username = User.get()
    password = Password.get()
    if username == "u" and password == "p":
        Log_in_label.config(text="Login successful. Let's get started.", fg="green")
        UI.after(2000, UI.destroy)
    else: # logs failed attempts
        global attempts
        attempts -= 1
        Log_in_label.config(text=f"Login failed. You have {attempts} left. ", fg="red")
        if attempts <= 0: # ends program after 3 failed attempts
            Log_in_label.config(text="Login failed. No attempts left.", fg="red")
            UI.after(1000, exit) 

# logic for training
def course(QA_Bank):
    global Wallet
    points_earned =  0 
    while True: 
        while points_earned < 50:
            question = choice(QA_Bank) # randomly selects a question from the question bank
            while True: # loops until user gives a valid answer
                if question["is_challenge"] == True:
                    print("⭐ Challenge question ⭐\n"
                        "Get it " + Fore.GREEN + "correct" + Style.RESET_ALL+ " for 10 points\n"
                        "Get it " + Fore.RED + "wrong" + Style.RESET_ALL+ " and lose 10 points")  
                    input("Press any key to continue: \n") #Pauses the program so the user can see their items  
                print(question['scenario'])
                sleep(2)
                for option, text in question['options'].items(): #Loops through options and displays in readable format. 
                    print(f"{option}: {text}")
                answer = input("\nYour answer: ").upper() #User's answer, starts anew line for enhanced readability
                if answer not in question['options']:
                    print(Fore.RED + "Invalid option. Please choose a valid option.")
                    return course(QA_Bank) # loops back to the question if an invalid option is chosen
                if answer == question['correct_answer']:
                    print(Fore.GREEN + "Correct!")
                    sleep(1)
                    match question['is_challenge']: # checks if the question is a challenge question to determine points earned
                        case True:
                            points_earned += 10
                            print(Fore.GREEN +"10 points have been added")
                            print(Fore.GREEN + f"Good job you have {points_earned} points.")
                            input("Press any key to continue: \n") #Pauses the program so the user can see their points
                            continue # loops back for the next question
                    
                        case False:
                            points_earned += 5
                            print(Fore.GREEN +"5 points have been added")
                            print(Fore.GREEN + f"You have {points_earned} points.")
                            input("Press any key to continue: \n") #Pauses the program so the user can see their points
                            continue # loops back for the next question
                else:
                    print(Fore.RED + "Incorrect.")
                    print(f"Explanation: {question['explanation']}\n")
                    input("Press any key to continue: \n") #Pauses the program so the user can see the explanation
                    if question["is_challenge"]: # If the question is a challenge question, the user loses points for getting it wrong. 
                        points_earned -= 10  
                        print(Fore.RED +"10 points have been deducted")
                        print(Fore.RED +f"You have {points_earned} points.")
                        input("Press any key to continue: \n") #Pauses the program so the user can see their points
                    continue # loops back for the next question
        if points_earned >= 50:
            Wallet += points_earned
            print(Fore.GREEN + f"Congratulations!{Style.RESET_ALL} You have completed the course.")
            print(f"You now have {Wallet} points to spend at the shop.")
            input("Press any key to continue:  ") #Pauses the program so the user can see read output 

#shop module for user to buy items with points, view their items.  
def shop():
    global Wallet
    print(f"Welcome to the shop!\nYou have {Wallet} points to spend.")
    while True: #Loop that keeps the shop running until the user chooses to leave.
        choice = input("Please choose one of the following options:\nBuy (A)\nView owned items (B)\nLeave (C)\nYour option: ").upper()
        match choice:
            case "A":
                for item, (price, input_number) in items.items(): #Loops though items in the shop and displays them in a readable format, with the price and the item.
                    print(f"{item}: {price} points ({input_number})")
                Purchase = input("Please input the number in brackets for the item you wish to purchase: ")
                for item, (price, input_number) in items.items():
                    if Purchase == input_number: #Only goes through buying process if the user input matches the item number
                        if Wallet >= price:
                            Wallet -= price
                            Owned_items.append(item)
                            print(f"You have purchased {item}  for {price} points. You have {Wallet} points left.")
                        else:
                            print("You do not have enough points to purchase this item.")
            case "B":
                print(f"You own these items:")
                for item in Owned_items: #Loops through the items the user has purchased and displays them.
                    print(item)
                input("Press any key to continue: \n") #Pauses the program so the user can see their items 
            case "C":
                print("Thank you for visiting the shop!")
                return
            case _:
                print("Invalid option, please try again.")
#sets up UI
UI.title("KFC Scenario Simulator")
UI.configure(bg = "#00BAFF")
Username_label = Label(UI, text="Username", font=("Arial", 18),  bg="#00BAFF")
User.config(bg = "#FFFFFF", font=("Arial", 18), width=30, borderwidth=2,)
Password_label = Label(UI, text="Password", font=("Arial", 18), bg="#00BAFF")
Password.config(bg = "#FFFFFF", font=("Arial", 18), width=30, borderwidth=2,)
Login = Button(UI, text="Log in", font=("Arial", 18), bg="#FF0000", width=20, borderwidth=2, command = login)
Log_in_label = Label(UI,text= "", fg="black", bg="#00BAFF", font=("Arial", 19))
UI.resizable(False, False) # doens't allow the user to resize the window

#Using Grid to set it all up
Username_label.grid(row=0, column=0, padx=10, pady=10)
User.grid(row=0, column=1, padx=10, pady=10)
Password_label.grid(row=1, column=0, padx=10, pady=10)
Password.grid(row=1, column=1, padx=10, pady=10)
Login.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
Log_in_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

UI.mainloop() #loads the window

while True:
    Course = input("Choose an option using the letters in the brackets:\n (A) Chicken cooking and handling \n (B) Health and safety procedures \n (C) Go to shop \n Your Input: ").upper()
    match Course: # casewhere statement in python to check the user's input
        case "A":
            #QA_Bank is a tuple of dictionaries, each containing all the information required by the program 
            QA_Bank = ({
                    'id': 1,
                    'scenario': 'The refrigerator temperature reads 8°C. Should you:',
                    'options': {
                        'A': 'Continue using it - close enough',
                        'B': 'Report it to management immediately',
                        'C': 'Try to adjust temperature yourself',
                        'D': 'Move all food to another fridge\n'
                    },
                    'correct_answer': 'B',
                    'explanation': 'Temperature control issues must be reported immediately.',
                    'is_challenge': False
                },
            {
                "id": 2,
            "scenario": "You have have the following batches to cook: 1 bag of OR chicken, 2 bags of tenders, and 1 bag of zinger fillets.\n Which batch should you cook first?",
            "options": {
                    "A": "Cook the OR chicken first",
                    "B": "Cook the tenders first",
                    "C": "Cook the zinger fillets first",
                    "D": "Cook whichever batch you feel like first"
            },
            "correct_answer": "A",
            "explanation": "The OR chicken has takes the longest time to cook so it should be cooked first, unless your manger specifies otherwise.",
            "is_challenge": True
            },
            {
            'id': 3,
            'scenario': 'You have loaded the fryers and finished cooking. What colour chux do you pcik to clean the fryers with? ',
            'options': {
                'A': "Green",
                'B': "Blue",
                'C': 'Red',
                'D': "Purple"
            },
            'correct_answer': 'C',
            'explanation': "You must always use the Red chux after to clean the fryers to prevent decomtamination.",
            'is_challenge': False
            },
            {
            'id': 4,
            'scenario':  "It is a busy night and we need to make sure the chicken texture is as good as possible. What strategy do we use to maintain the flour to prevent clumps? ",
            'options': {
                'A': "Sift and top the lugs up as you alternate between them, when they need to.",
                'B': "Save sifting for the end" ,
                'C': "Only do it when you need to",
                'D': "Do it after every bag", 
            },
            'correct_answer': "A",
            'explanation': "Sifting and topping up the flour as you go, ensures that the flour is top quality while allowing you to bread all the chicken quickly.",
            'is_challenge': True
            },
            {'id':5 ,
         'scenario': "You have recieved a batch of chicken to cook. What is the first thing you do?" ,
         'options': {
               'A': "get to it immediately",
               'B': "wash hands and put gloves and apron on ",
               'C': "Continue what I was doing",
               'D': "Get the chicken",
         },
         'correct_answer': "B",
         'explanation': "Since you are working with raw chicken, hygiene is important.",
         'is_challenge': False
         },
         {'id':6 ,
         'scenario': "You have just clocked in for your shift. What is the first thing you do?" ,
         'options': {
               'A': "Start your tasks",
               'B': "Set up your station",
               'C': "Inquire about any specials or important information for the day",
               'D': "Wash your hands",
         },
         'correct_answer': "D",
         'explanation': "No matter what. The first you do is wash your hands, after clocking in. No excuses allowed",
         'is_challenge': False
        },
        {'id':7 ,
         'scenario': "Huh that is wierd? What is the fryer doing?", 
         'options': {
               'A': "I am going to aks the manager",
               'B': "Let's just ignore it",
               'C': "I am evacuating. RUN RUN RUN.", 
               'D': "We need to investigate"
         },
         'correct_answer': "A",
         'explanation': "Chances are it is completely normal so ask just ask someone. If it does need investigating, inform the manager on duty. They will know what to do.",
         'is_challenge': False 
        }




            )
            course(QA_Bank)
        case "B":
            QA_Bank = ({
        'id': 1,
        'scenario': 'You notice that the oil in the fryer has turned dark and has a strong odor. What should you do?',
        'options': {
            'A': 'Continue using it until the end of the shift',
            'B': 'Add fresh oil to dilute the old oil',
            'C': 'Report it to the manager and follow the oil filtering/changing procedure',
            'D': 'Turn off the fryer and leave it for the next shift'
        },
        'correct_answer': 'C',
        'explanation': 'Degraded oil affects food quality and safety. Report it to your manager and follow proper oil changing procedures.',
        'is_challenge': False
    },
    {
        'id': 2,
        'scenario': 'You are about to enter the walk-in cooler to grab chicken after breading up a batch. Which colour handle do you use?',
        'options': {
            'A': 'Red',
            'B': 'Green',
            'C': 'Whichever one',
            'D': 'They are just decorative and have no specific purpose'
        },
        'correct_answer': 'A',
        'explanation': 'You are contamineted with raw chicken so you will use the red handle. Green is uncontaminated people. ',
        'is_challenge': False
    },
    {
        'id': 3,
        'scenario': 'You accidentally spill hot oil on the floor near the fryer station. What is your first action?',
        'options': {
            'A': 'Continue working and clean it up later when less busy',
            'B': 'Warn nearby team members, block off the area, and begin proper cleanup procedures',
            'C': 'Pour water on it to cool it down quickly',
            'D': 'Cover it with cardboard boxes until it cools'
        },
        'correct_answer': 'B',
        'explanation': 'Hot oil spills are serious hazards requiring immediate action. Warn others, block the area, and never use water on hot oil.',
        'is_challenge': False
    },
    {
        'id': 4,
        'scenario': 'A team member in the kitchen has a visible cut on their hand. What is the correct procedure?',
        'options': {
            'A': 'They can continue working as long as they wash their hands frequently',
            'B': 'Apply a blue detectable bandage and wear a food-safe glove over the wound',
            'C': 'Cover with a regular bandage and continue handling food',
            'D': 'Send them home immediately regardless of wound severity'
        },
        'correct_answer': 'B',
        'explanation': 'Blue detectable bandages are visible if they fall off and can be detected by metal detectors. A food-safe glove must be worn over the bandage.',
        'is_challenge': True
    },
    {
        'id': 5,
        'scenario': 'How often should you wash your hands during your shift?',
        'options': {
            'A': 'Only at the start and end of your shift',
            'B': 'Every 30 minutes regardless of tasks',
            'C': 'After handling raw chicken, using the restroom, touching your face, handling trash, and before starting food prep',
            'D': 'Only when your hands are visibly dirty'
        },
        'correct_answer': 'C',
        'explanation': 'Handwashing must occur at critical control points to prevent cross-contamination. This includes after handling raw products, using the restroom, and before food prep.',
        'is_challenge': False
    },
    {
        'id': 6,
        'scenario': 'You are breading chicken and notice that a batch has been sitting at room temperature for 3 hours. What should you do?',
        'options': {
            'A': 'Use it quickly before it goes bad',
            'B': 'Put it back in the cooler to bring the temperature down',
            'C': 'Discard the chicken and report the incident to your manager',
            'D': 'Smell the chicken to check if it is still good'
        },
        'correct_answer': 'C',
        'explanation': 'Chicken in the danger zone (4°C-60°C) for over 2 hours must be discarded. Bacteria multiply rapidly making food unsafe regardless of smell or appearance.',
        'is_challenge': True
    },
    {
        'id': 7,
        'scenario': 'What type of footwear should be worn in the KFC back of house area?',
        'options': {
            'A': 'Any comfortable closed-toe shoes',
            'B': 'Non-slip, closed-toe shoes with oil-resistant soles',
            'C': 'Steel-toe boots only',
            'D': 'Sneakers with good grip'
        },
        'correct_answer': 'B',
        'explanation': 'Non-slip, oil-resistant shoes prevent slips and falls in the kitchen. This protects against injuries from hot oil and wet floors.',
        'is_challenge': False
    })
            course(QA_Bank)
        case "C":
            shop() 
        case _:
            print("Invalid option. Please choose A, B, or C.")
            continue # loops back to the input prompt if an invalid option is chosen
   

    
