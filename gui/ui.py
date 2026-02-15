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
    title_label = Label(root, textvariable=title, bg="#111", fg="#fff", 
          font=("Arial", 20, "bold"), height=2)
    
    select = StringVar(value="Select file type to generate:")
    select_label = Label(root, textvariable=select, bg = "#000", fg="#fff", 
          font=("Arial", 14, "bold"),
          height=1)
    
    choice = StringVar()
    options = [".txt",".csv"]
    choice.set(".txt")
    menu = ttk.Combobox(root, textvariable=choice, state="readonly")
    menu["values"] = options

    button = Button(root, text="GENERATE", bg="lime", fg="#fff", 
                    font=("Arial", 20, "bold"), width=15, height=2)
    
    title_label.pack(fill="x", padx=10, pady=10)
    select_label.pack()
    menu.pack(pady=10)
    button.pack(padx=5, pady=(100, 0))

    # bind to generate later
    #root.bind("<Return>", None)

    root.mainloop()

