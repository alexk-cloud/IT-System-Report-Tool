from tkinter import *
from tkinter import ttk
from system_report import *

def run_gui():
    root = Tk()

    root.title("System Report Tool")
    root.geometry("600x400")
    root.resizable(False, False)
    root.configure(bg="#000")

    title = StringVar(value="System Report Tool")

    Label(root, textvariable=title, bg="#111", fg="#fff", 
          font=("Arial", 20, "bold"),
          height=2).pack(fill="x", padx=10, pady=10)
    
    # bind to generate later
    #root.bind("<Return>", None)

    root.mainloop()

