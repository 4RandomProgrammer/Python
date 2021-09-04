import tkinter as tk
from tkinter import *

root = tk.Tk('Tryout app')

def toDarkMode():
    canvas.configure(bg="black")
    frame.configure(bg="black")
    myLabel.configure(text="In dark Mode",fg="white", bg="black")

def toWhiteMode():
    canvas.configure(bg="white")
    frame.configure(bg="white")
    myLabel.configure(text="In white Mode",fg="black", bg="white")

#Preciso saber a diferença entre usar um canvas e settar o geometry
canvas = tk.Canvas(root, height=500, width=600, bg="white")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.6, relwidth=0.6, relx=0.2, rely=0.2)

myLabel = tk.Label(frame,text="in White mode", fg="black", bg="white")
myLabel.pack()

darkMode = tk.Button(root, text="To Dark Mode", fg="white", bg="black", command=toDarkMode)
darkMode.pack()


whiteMode = tk.Button(root, text="To white mode", fg="black", bg="white", command=toWhiteMode)
whiteMode.pack()


root.mainloop()