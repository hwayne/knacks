from csv import DictReader, DictWriter
from random import random, shuffle
from datetime import date
from tkinter import N, S, E, W, ttk
import tkinter as tk

"""
1. Read in csv of friends
2. For each friend, generate a rand()
3. If rand ≤ 1/time, mark friend to list
4. Create a GUI with each marked friend and a checkmark
5. For each checked friend (probably up to 2), add to the contact CSV
"""

candidates = []
with open("path/to/friendlist.csv") as f:
    reader = DictReader(f)

    for person in reader:
        if random() < 1/int(person["Days"]):
            candidates.append(person)


shuffle(candidates) # So if we go down from the top with a limit, it's more distributed

root = tk.Tk()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.bind("<Escape>", lambda _: root.quit())
root.bind("<Return>", lambda _: root.quit())

choices = []
boxes = []

# Needs to be a generator to get around Python's weird scoping rules with lambdas
handlergen = lambda i: lambda _: boxes[i].invoke()

for i, c in enumerate(candidates):
    selected = tk.IntVar()
    choices.append(selected)

    checkbox = tk.Checkbutton(mainframe, variable=selected)
    name =  tk.Label(mainframe, text=c["Name"])
    method =  tk.Label(mainframe, text=c["Contact"])
    comments =  tk.Label(mainframe, text=c["Comments"])


    checkbox.grid(column=0, row=i)
    name.grid(column=1, row=i, sticky=W)
    method.grid(column=2, row=i, sticky=W)
    comments.grid(column=3, row=i, sticky=W)
    if i < 9:
        boxes.append(checkbox)
        root.bind(f"<Key-{i+1}>", handlergen(i))

root.mainloop()

with open('path/to/contacts.csv', 'a') as csvfile:
    writer = DictWriter(csvfile, fieldnames=['Name', 'Date'])
    for i, c in enumerate(candidates):
        if choices[i].get():
            writer.writerow({"Name": c["Name"], "Date": date.today()})
