def get_user_in():
    program = []

    print("Type you NotBasic program below. To finish the program create a new line and type `eof` and press enter.")

    while True:
        inp = input('> ')

        if inp == "eof":
            break

        program.append(inp)

    return program