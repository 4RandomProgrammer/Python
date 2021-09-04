import tkinter as tk
from tkinter import Button, Canvas, Label, filedialog, Text
import os



#Root = body
root = tk.Tk('App by Dev Ed')
apps = []


if os.path.isfile('save.txt'):
    with open('save.txt', r) as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = tempApps
        print(tempApps)
        apps = [x for x in tempApps if x.strip()]

def Addap():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select file: ", filetypes=(("executable", "*.exe"), ("all file", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        myLabel = tk.Label(frame, text=app, bg="gray")
        myLabel.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

btn = tk.Button(root, text="Open file", padx=10, pady=5, fg="white", bg="black", command=Addap)
btn.pack()
btn2 = tk.Button(root, text="Run as", padx=10, pady=5, fg="white", bg="black", command=runApps)
btn2.pack()

for app in apps:
    olderLabel = tk.Label(frame, text=app)
    olderLabel.pack()

root.mainloop()

with open('save.txt', w) as f:
    for app in apps:
        f.write(app + ',')