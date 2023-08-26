from stdout import *

from stdout import console_setup

def credit_menu(screen):
    console_setup(screen)

    print_centered(screen, "Created by Lachlan Jowett", -1)

    print_centered(screen, "[ Press any key to return to the main menu ]", 1)

    screen.getch()

    return

