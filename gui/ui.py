from tkinter import *
from tkinter import ttk
from system_report import *

def run_gui():
    root = Tk()

    window_width = 600
    window_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.title("System Report Tool")
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)
    
    root.configure(bg="#000")

    title = StringVar(value="System Report Tool")

    Label(root, textvariable=title, bg="#111", fg="#fff", 
          font=("Arial", 20, "bold"),
          height=2).pack(fill="x", padx=10, pady=10)
    
    # bind to generate later
    #root.bind("<Return>", None)

    root.mainloop()

