from tkinter import * 
UI = Tk()
User = Entry()

UI.title("KFC training program")
UI.configure(bg = "#00BAFF")
Log_in_label = Label(UI, text="Log in", font=("Arial", 24, "bold"), bg="#00BAFF")
Log_in_label.pack(pady=20)

Username_label = Label(UI, text="Username", font=("Arial", 18),  bg="#00BAFF")
Username_label.pack(pady = 10, side= TOP,anchor="w")

Password_label = Label(UI, text="Password", font=("Arial", 18), bg="#00BAFF")
Password_label.pack(pady= 10, side = BOTTOM,anchor= "w")

UI.mainloop() #loads the window