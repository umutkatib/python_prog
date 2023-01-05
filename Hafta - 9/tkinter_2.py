from tkinter import *

window = Tk()

window.title("Python GUI")
lbl = Label(window, text="Hello")
lbl2 = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')
window.mainloop()