from stdout import *

def get_lists():
    lists = open("lists.txt", "r").read()

    return lists.split("\n")

def grocery_list_input_manager():
    ...

def grocery_list_manager_menu(screen):
    console_setup(screen)

    print_centered(screen, "[                                              Delete list: | ALT + r | ]", int((TERMINAL_HEIGHT_CHARACTERS / 2) - 1))

    screen.getch()
