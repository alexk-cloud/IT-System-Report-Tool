import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from system_report import *

def browse_directory():
	return filedialog.askdirectory()

def shorten_path(path):
	if len(path) >= 50:
		return path[:25] + "..." + path[-20:]
	
	return path

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
	
	status_msg = StringVar()
	status_label = Label(root, textvariable=status_msg, fg="#fff", bg="#000",
			font=("Arial", 12))
	status_label.pack(side="bottom", pady=10)
	
	def handle_browse():
		path = browse_directory()

		if path:
			folder_path.set(shorten_path(path))

	dir_button = Button(text="Browse directory", font=("Arial", 12), command=handle_browse)
	dir_button.config(relief="flat")

	def handle_gen():
		selected_dir = folder_path.get()
		
		if not selected_dir:
			status_msg.set("Please select a directory!")
			status_label.config(fg="red")
			return
		
		try:
			os.makedirs(selected_dir, exist_ok=True)
		except PermissionError:
			status_msg.set("Cannot create files: permission denied.")
			status_label.config(fg="red")
			return
		except OSError as e:
			status_msg.set(f"Error creating files: {e}")
			status_label.config(fg="red")
			return

		info = get_system_info()
		ping = ping_test()
		procs = get_top_processes()

		file_type = choice.get()

		if file_type == ".txt":
			make_txt(info, ping, procs, output_dir=selected_dir)
			status_msg.set(f".txt report generated at {shorten_path(selected_dir)}.")
			status_label.config(fg="lime")
		else:
			make_csv(info, procs, selected_dir)
			status_msg.set(f".csv summary generated at {shorten_path(selected_dir)}.")
			status_label.config(fg="lime")
	
	gen_button = Button(root, text="GENERATE", bg="lime", fg="#fff", 
					font=("Arial", 20, "bold"), width=15, height=1)
	gen_button.config(command=handle_gen)
	
	title_label.pack(fill="x", padx=10, pady=10)
	select_label.pack()
	menu.pack(pady=10)
	select_dir_label.pack()
	dir_label.pack(pady=10)
	dir_button.pack(pady=10)
	gen_button.pack(padx=5, pady=(10, 0))
	
	root.mainloop()

