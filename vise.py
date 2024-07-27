import curses
from curses import wrapper
import time


def main(stdscr):

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    window = curses.newwin()
    for i in range(10):
        stdscr.clear()
        stdscr.addstr(f"Enter file path [{i + 1}]: ", curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.5)
    stdscr.getch() # Initialize the window and set the border
    

wrapper(main)