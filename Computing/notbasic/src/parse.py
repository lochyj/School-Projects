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
                            bound_line.append(word)
                            word = ""
                    case '\"':
                        if reading_string:
                            if j > 1:
                                if line[j - 1] == '\\':
                                    ...
                                else:
                                    ... # EoS
                            else:
                                ... # EoS

                        else:
                            ...


            bound_lines.append(bound_line)

    def parse(self, lines):

        lines = self.strip_comments(lines)
        lines = self.remove_blank_lines(lines)
        lines = self.bind_lines(lines)

        parsed_lines = []

        for params in lines:
            if len(params) < 3:
                print("")

            line_num = params[0]
            operator = params[1]

            params.pop(0); params.pop(0)


            # line_num: int, operator: str, params: list[str]
            parsed_lines.append((line_num, operator, params))

        return parsed_lines