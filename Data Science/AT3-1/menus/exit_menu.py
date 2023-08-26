from stdout import *

def exit_menu(screen):
    screen.refresh()

    console_setup(screen)

    print_centered(screen, "[ Press any key to exit ]", 0)

    screen.getch()
    screen.clear()