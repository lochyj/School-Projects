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

# The stdout.py file contains utility functions for manipulating and using the stdout features of curses, it extends the library to make it easier and cleaner to use.

import curses

# ----------|
# Constants |
# ----------|

TERMINAL_WIDTH_CHARACTERS = 80
TERMINAL_HEIGHT_CHARACTERS = 24

# ----------|
# Functions |
# ----------|

def print_centered(screen, text, y_offset = 0):
    screen.addstr(curses.LINES // 2 + y_offset, curses.COLS // 2 - len(text) // 2, text)

def print_centered_selected(screen, text, y_offset = 0):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    screen.addstr(curses.LINES // 2 + y_offset, curses.COLS // 2 - len(text) // 2, text, curses.color_pair(1))

def console_setup(screen):
    curses.resize_term(TERMINAL_HEIGHT_CHARACTERS, TERMINAL_WIDTH_CHARACTERS)

    screen.clear()
    screen.refresh()

    curses.curs_set(0)

    # Use the default curses border
    screen.border()

    #init_colors(screen)

    screen.refresh()
