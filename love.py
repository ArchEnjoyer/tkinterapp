from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
def funct1():
    messagebox.showinfo(" ", "А я люблю тебя!!!")
    quit()
def funct2(param):
    btnNO.place(x=random.randint(100, 1000), y=random.randint(100, 750))

borderImageData = '''
    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
'''

root = Tk()
root.geometry('1200x800')
root.title("Любовь")
root.resizable(0,0)
root["bg"] = 'pink'

style = ttk.Style()
borderImage = PhotoImage("borderImage", data=borderImageData)
style.element_create("RoundedFrame",
                     "image", borderImage,
                     border=25, sticky="nsew")
style.layout("RoundedFrame",
             [("RoundedFrame", {"sticky": "nsew"})])

frame1 = ttk.Frame(style="RoundedFrame", padding=15)
text2 = Label(frame1, text="Любишь ли ты меня?", font="Arial 24 bold", bg='#f1396b', borderwidth=0, highlightthickness=0, width=20, height=2).pack()
frame1.pack(side="top", padx=20, pady=20)

btnYES = Button(root, text="Да", font="Arial 24 bold", bg='#f1396b', command=funct1)
btnYES.place(x=200, y=200)
btnNO = Button(root, text="Нет", font="Arial 24 bold", bg='#f1396b')
btnNO.bind('<Enter>', funct2)
btnNO.place(x=800, y=200)



root.mainloop()
