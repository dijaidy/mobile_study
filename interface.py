from tkinter import *

window = Tk()

window.title("MOBILE_STUDY")
window.geometry("400x800")

font = ("BMJUA_ttf",)
label = Label(window, text="MOBILE\nSTUDY")
label.place(relx=0, relwidth=1, rely=0, height=50)


window.resizable(width=False, height=False)
window.mainloop()
