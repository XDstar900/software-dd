from tkinter import * 


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



#sets up UI
UI.title("KFC training program")
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
        Course = input("Choose an option using the letters in the brackets:\n (A) Chicken handling \n (B) Health and safety procedures \n (C) Go to shop \n").upper()
        match Course: # casewhere statement in python to check the user's input
            case "A":
                print("Chicken handling")
            case "B":
                print("Health and safety procedures")
            case "C":
                print("Go to shop")
            case _:
                print("Invalid option. Please choose A, B, or C.")
                continue # loops back to the input prompt if an invalid option is chosen