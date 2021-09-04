from tkinter import *


root = Tk()
root.title('Henlo')
root.geometry("400x400")



def henlo():
    hello_label = Label(root, text="Hello " + myTextbox.get())
    hello_label.pack()



#label
myLabel = Label(root, text="Enter your first name:")

#put on the very first spot
#grid vc diz exatamente onde tem que ir
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=henlo)
myButton.pack()



root.mainloop() #como o programada detecta o que etsa acontecendo