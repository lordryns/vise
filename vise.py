import curses
from curses import wrapper
import time


def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)


    window_height, window_width = stdscr.getmaxyx()
    window = curses.newwin(window_height, window_width, 0, 0)
    for i in range(10):
        window.clear()
        window.addstr(f"Enter file path [{i + 1}]: ", curses.color_pair(1))
        window.refresh()
        time.sleep(0.5)
    

wrapper(main)