import rich 
from rich.console import Console
import time


console = Console()

console.print("[cyan]Hello [/]world, this was built with [yellow]Python.")

name = console.input("Enter your name: ")
with console.status("Loading", spinner='aesthetic'):
	time.sleep(3)
	console.print("Almost there...")
	time.sleep(3)
	console.print("Done!", style="green")
	time.sleep(1)


console.clear()