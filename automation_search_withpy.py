import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

#Adding a background color
root.configure(bg='steelblue')

#Define the fuction to automate youtube search
def search_youtube():
    query=entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query=entry.get()
    url = f"https://www.google.com/search?search_query={query}"
    webbrowser.open(url)

def search_instragram():
    Username = entry.get().replace('@',"") #Ensure username is clean of '@'
    url = f"www.instragram.com/{Username}/"
    webbrowser.open(url)

#create input field. Labels and buttons
Label(root, text = "Enter your command: ").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Serach on Youtube", command = search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instragram", command=search_instragram).pack(pady=5)

#Run the GUI event loop
root.mainloop()