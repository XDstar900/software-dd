import tkinter as tk
UI = tk.Tk()
UI.title("KFC training program")
Icon = tk.PhotoImage(file="kfc-icon.png")
UI.iconphoto(True, Icon)
UI.geometry("800x600")
UI.configure(bg = "#00BAFF")
Log_in_label = tk.Label(UI, text="Log in", font=("Arial", 24, "bold"), bg="#00BAFF")
Log_in_label.pack(pady=20)
Username_label = tk.Label(UI, text="Username", font=("Arial", 18),  bg="#00BAFF")
Username_label.pack(pady = 10)
Password_label = tk.Label(UI, text="Password", font=("Arial", 18), bg="#00BAFF")
Password_label.pack(pady= 10)

UI.mainloop() #loads the window