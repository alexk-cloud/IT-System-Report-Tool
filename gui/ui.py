from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from system_report import *

def browse_directory():
	return filedialog.askdirectory()

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

	select_dir = StringVar(value="Choose output directory:")
	select_dir_label = Label(root, textvariable=select_dir, bg = "#000", fg="#fff", 
			font=("Arial", 14, "bold"),
			height=1)
	
	folder_path = StringVar()
	dir_label = Label(root, textvariable=folder_path, bg="#fff", fg="#000",
			font=("Arial", 10), width=50, height=2)
	
	gen_button = Button(root, text="GENERATE", bg="lime", fg="#fff", 
					font=("Arial", 20, "bold"), width=15, height=1)
	
	def handle_browse():
		path = browse_directory()

		if path:
			folder_path.set(path)
			print(f"Selected path: {path}")
	
	dir_button = Button(text="Browse directory", font=("Arial", 12), command=handle_browse)
	dir_button.config(relief="flat")

	title_label.pack(fill="x", padx=10, pady=10)
	select_label.pack()
	menu.pack(pady=10)
	select_dir_label.pack()
	dir_label.pack(pady=10)
	dir_button.pack(pady=10)
	gen_button.pack(padx=5, pady=(10, 0))
	
	# bind to generate later
	#root.bind("<Return>", None)

	root.mainloop()

