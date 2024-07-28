import rich 
from rich.console import Console
import time
import os


console = Console()
console.set_window_title("Vise 1.0")
console.clear()

current_file = None 

def open_file_to_edit() -> bool:
	global current_file
	run = True 
	while run: 
		path = console.input("Enter the path of the file you want to edit: ")

		if os.path.exists(path):
			current_file = path
			console.print(f"{path.split("/")[-1]} opened successfully!", style="green")
			run = False
			return True
	
		else:
			console.print("File does not exist, perharps a typo?", style="red")

		console.input("")
		console.clear()
		

	return False

can_launch_editor: bool = open_file_to_edit()

if can_launch_editor: 
	console.print("Hold on, setting up editor...")
	with console.status("setting up..."):
		time.sleep(1)
		console.clear()
		console.print("Done!", style="green")


