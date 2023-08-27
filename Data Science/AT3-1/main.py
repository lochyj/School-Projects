#   MIT License
#
#   Copyright (c) 2022 Lachlan Jowett
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

# --------------|
# Prerequisites |
# --------------|

# For windows:
# pip install windows-curses

# ----------------------|
# Precursor information |
# ----------------------|

# Curses is a terrible library. Its old and undocumented.
# It also had a really bad and inconsistent naming scheme which makes creating easy to understand code really really annoying.

# --------|
# Imports |
# --------|

import os
import sys
import math

# Because curses is a posix standard and windows likes to be different.
# Check if the user is on windows.
# If so, tell the user to install the windows-curses package if it isn't already.
# This is because the python default curses library doesn't work on windows.
try:
    import curses
    from curses import wrapper
except ImportError:
    if os.name == "nt":
        print("\
            WARN: Curses isn't natively supported by windows, please install the windows-curses package that makes curses compatible with windows.\n\
            Run `pip install windows-curses` to install it.\
        ")
    else:
        print("WARN: Usually this should never happen, the curses library is built into python and should in theory be compatible with your OS by default.")

    exit(-1)


# Importing our py files, we do this here because we need to include the curses library in each file and it may not work if we do it first
from stdout import *
from color import *
from menus.main_menu import *
from menus.exit_menu import *

# -----

def handle_input(screen, current_menu_wrapper):
    key = screen.getch()

    print_centered(screen, "                    ", 5)

    match key:
        case 258:   # Down arrow key
            main_menu_input_handler(screen, "DOWN")
        case 259:   # Up arrow key
            main_menu_input_handler(screen, "UP")

        case 27: # Escape key / ALT + [key]
            # We need to disable the delay so we can get the extra info from the key press to determine if it is an alt key or an escape key
            screen.nodelay(True)
            key_extention = screen.getch()
            screen.nodelay(False)

            match key_extention:
                case -1:
                    ...
                    # Escape key has been pressed

            # Handle alt keys if needed...

        case 10: # Enter key

            if current_menu_wrapper == main_menu:
                if main_menu_input_handler(screen, "ENTER") == True:
                    return True

                return

        case 433:   # Alt + q, We need to quit the application!
            return True

        case other:
            print_centered(screen, str(key), 5)

def program_entry(screen):

    console_setup(screen)

    main_menu(screen)

    screen.refresh()

    while True:
        if handle_input(screen, main_menu) == True:
            break

    exit_menu(screen)



# Get curses to run our program using the wrapper library. This is much cleaner that using the curses.initscr() method.
wrapper(program_entry)