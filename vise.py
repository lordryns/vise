import rich 
from rich.console import Console
import time
import os


def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')



console = Console()
console.set_window_title("Vise 1.0")
clear_screen()

current_file = ""



def open_file_to_edit() -> bool:
	global current_file
	run = True 
	while run: 
		path = console.input("Enter the path of the file you want to edit: ")
		path = path.replace(" ", "")

		if os.path.exists(path):
			current_file = path
			split_path = path.split("/")[-1]
			console.print(f"{split_path} opened successfully!", style="green")
			run = False
			return True
	
		else:
			console.print("File does not exist, perharps a typo?", style="red")

		console.input("")
		clear_screen()
		

	return False

can_launch_editor: bool = open_file_to_edit()


# the editor screen 
def text_editor(file_path: str) -> None:
	console.print(f"file open: [green]{file_path}")

	try:
		with open(file_path,'r') as fp:
			lines = fp.readlines()

		for i, line in enumerate(lines):
			console.print(f"{i+1} {line}")
	except Exception as e:
		console.print(f"Error: [red]{e}")

if can_launch_editor: 
	console.print("Hold on, setting up editor...")
	with console.status("setting up..."):
		time.sleep(1)
		console.clear()
		

text_editor(file_path=current_file)


