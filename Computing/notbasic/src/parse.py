def parse(lines):

    parsed_lines = []

    for line in lines:

        if line == '':
            continue

        if line.startswith(';'):
            continue

        line = line.strip()
        split_line = line.split(' ')
        line_num = split_line[0]
        operator = split_line[1]

        if (operator == ';'):
            continue

        split_line.pop(0); split_line.pop(0)

        reading_string = False
        string = ""

        params = []

        for param in split_line:

            if param.startswith(';') or param == ';':
                break

            if param.startswith('\"'):
                reading_string = True
                param.removeprefix('\"')

                if param.endswith('\"'):
                    param.removeprefix('\"')
                    string += f"{param}"

                    params.append(("str", string))

                    reading_string = False
                    string = ""
                    continue

                string += f"{param} "
                continue

            if reading_string and param.endswith('\"'):
                param.removeprefix('\"')
                string += f"{param}"

                params.append(("str", string))

                reading_string = False
                string = ""
                continue

            params.append(param)



        # line_num: int, operator: str, params: list[str]
        parsed_lines.append((line_num, operator, params))

    return parsed_lines