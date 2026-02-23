from tkinter import *
window = Tk()
window.title("Trainee login")
window.geometry("600x800")
label = Label(window, text="Enter your details to get started")
label.pack()
button = Button(window, text="Click Me", fg='blue')
button.pack()
window.mainloop()   
