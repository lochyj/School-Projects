from stdout import *

from menus.manager_menu import *
from menus.credit_menu import *

main_menu_options = [
    "[ Grocery List Manager ]",
    "[        Credit        ]",
    "[         Exit         ]"
]

main_menu_selected_option = 0
def main_menu(screen, selected_option = 0):
    console_setup(screen)

    print_centered(screen, "Lachlan's Grocery List Manager", -4)

    print_centered(screen, main_menu_options[0], -2)
    print_centered(screen, main_menu_options[1], -0)
    print_centered(screen, main_menu_options[2], 2)

    # convert the selected option to the position on the screen
    selected = (main_menu_selected_option * 2) - 2

    print_centered_selected(screen, main_menu_options[selected_option], selected)

def main_menu_input_handler(screen, key):

    # Python moment...
    global main_menu_selected_option

    match key:
        case "UP":
            main_menu_selected_option -= 1

            # Keep the selected option within the bounds of the menu options
            main_menu_selected_option %= len(main_menu_options)

            main_menu(screen, main_menu_selected_option)

        case "DOWN":
            main_menu_selected_option += 1

            # Keep the selected option within the bounds of the menu options
            main_menu_selected_option %= len(main_menu_options)

            main_menu(screen, main_menu_selected_option)

        case "ENTER":
            print_centered(screen, "You pressed enter on: " + str(main_menu_selected_option), 5)
            match main_menu_selected_option:
                case 0:
                    grocery_list_manager_menu(screen)
                    main_menu(screen)
                case 1:
                    credit_menu(screen)
                    main_menu(screen)
                case 2:
                    return True
