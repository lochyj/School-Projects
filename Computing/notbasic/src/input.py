
# A simple python like input system for when the user wants to use the interpreter in the command line.
def get_user_in():
    program = []

    print("Type your NotBasic program below. To finish the program create a new line and type `eof` and press enter.")

    while True:
        line = input('> ')

        if line == "eof":
            break

        program.append(line)

    return program