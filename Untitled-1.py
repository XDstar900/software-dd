from tkinter import * 
from random import choice
from colorama import 

colorama.init()

UI = Tk()
User = Entry()
Password = Entry()
attempts = 3

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

def course(QA_Bank):
    points_earned = 0 
    while points_earned < 50:
        if QA_Bank == False: 
            return # ends fucntion as user went to the shop.
        question = choice(QA_Bank) # randomly selects a question from the question bank
        while True: # loops until user gives a valid answer
            print(question['scenario'])
            for option, text in question['options'].items(): #Loops through options and displays in readable format. 
                print(f"{option}: {text}")
            answer = input("Your answer: ").upper()
            if answer not in question['options']:
                print("Invalid option. Please choose a valid option.")
                return course(QA_Bank) # loops back to the question if an invalid option is chosen
            if answer == question['correct_answer']:
                print("Correct!")
                match question['is_challenge']: # checks if the question is a challenge question to determine points earned
                    case True:
                        points_earned += 10
                    case False:
                        points_earned += 5
            else:
                print("Incorrect.")
                print(f"Explanation: {question['explanation']}")
                if question["is_challenge"]: # if the question is a challenge question, the user loses points for getting it wrong. 
                    points_earned -= 5  

#sets up UI
UI.title("KFC Scenario Simulator")
UI.configure(bg = "#00BAFF")
Log_in_label = Label(UI, text="Log in", font=("Arial", 24, "bold"), bg="#00BAFF")
Username_label = Label(UI, text="Username", font=("Arial", 18),  bg="#00BAFF")
User.config(bg = "#FFFFFF", font=("Arial", 18), width=30, borderwidth=2,)
Password_label = Label(UI, text="Password", font=("Arial", 18), bg="#00BAFF")
Password.config(bg = "#FFFFFF", font=("Arial", 18), width=30, borderwidth=2,)
Login = Button(UI, text="Log in", font=("Arial", 18), bg="#FF0000", width=20, borderwidth=2, command = login)
Log_in_label = Label(UI,text= "", fg="black", bg="#00BAFF", font=("Arial", 19))

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
            print("Chicken cooking and handling") #debug
            #QA_Bank is a list of dictionaries, each conaitng all the information required for question 
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
            'scenario': 'What colour chux do you need to use to clean the fryers after dropping a batch of chicken?',
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


            )
        case "B":
            print("Health and safety procedures") #debug
        case "C":
            print("Go to shop")
            QA_Bank = False # resets the question bank to prevent user from accessing it when they go to the shop and prevents crashing when they come out of shop. 
        case _:
            print("Invalid option. Please choose A, B, or C.")
            continue # loops back to the input prompt if an invalid option is chosen
    course(QA_Bank)   
    
    