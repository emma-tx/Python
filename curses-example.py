#Python curses example

#Import curses and system modules/APIs
from os import system
import curses

#Initialise the curses UI and declare myscreen namespace
myscreen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)

myscreen.border(0)

#Print string with addstr()
myscreen.addstr(5, 5, "HELLO WORLD", curses.color_pair(1))

#Get string using getstr() and declare as input
input = myscreen.getstr(12, 20, 50)

#Refresh screen and read escape character from keyboard
myscreen.refresh()
myscreen.getch()

#Exit curses window
curses.endwin()

