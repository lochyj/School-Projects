from src.types import *

class Analyzer:
    def __init__(self) -> None:
        self.lexicon = {
            "operations": [
                "print",
                "add",
                "sub",
                "store",
                "conf",
                "value",
                "dec",
                "inc",
                "jnz"
            ],
            "values": [
                "true",
                "false"
            ],
            "terminators": [
                "eof"
            ]
        }

    def extract_type(self, object):
        ...

    def strip_comments(self, lines: list[str]):
        for i, line in enumerate(lines):
            if ';' in line:
                cut_index: any = None
                for j, character in enumerate(line):
                    if character == ';':
                        cut_index = j
                        break

                if cut_index != None:
                    lines[i] = line[0:cut_index].strip()
                else:
                    ... # Something went terribly wrong...

        return lines

    def remove_blank_lines(self, lines: list[str]):
        index = 0

        blank_words = [
            '',
            '\n',
            '\r',
            "\r\n",
            "eof",
        ]

        while index < len(lines):
            line = lines[index]
            if line in blank_words:
                lines.pop(index)
                index -= 1

            index += 1

        return lines

    def classify_param(self, param: str, is_string):
        if is_string:
            return String(param)

        if param.isdigit():
            return Integer(param)

        return Variable(param)

    def bind_lines(self, lines):
        bound_lines = []

        for i, line in enumerate(lines):
            reading_string = False
            word = ""
            bound_line = []

            for j, character in enumerate(line):

                match character:
                    case ' ':
                        if reading_string:
                            word += character
                        else:
                            bound_line.append(self.classify_param(word, False))
                            word = ""

                    case '\"':
                        if reading_string:
                            if j > 1:
                                if line[j - 1] == '\\':
                                    word += '\"'
                                else:
                                    bound_line.append(self.classify_param(word, True))
                                    word = ""
                            else:
                                bound_line.append(self.classify_param(word, True))
                                word = ""

                        else:
                            reading_string = True

                    case _:
                        word += character

            bound_line.append(self.classify_param(word, reading_string))
            bound_lines.append(bound_line)

        return bound_lines

    def parse(self, lines):

        lines = self.strip_comments(lines)
        lines = self.remove_blank_lines(lines)
        lines = self.bind_lines(lines)

        parsed_lines = []

        for params in lines:
            if len(params) < 3:
                print("ERROR: Line doesn't have enough parameters.")
                print(params)
                exit()

            line_num = params[0].value
            operator = params[1].name

            params.pop(0); params.pop(0)


            # line_num: int, operator: str, params: list[str]
            parsed_lines.append((line_num, operator, params))

        return parsed_lines