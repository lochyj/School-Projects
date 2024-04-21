from src.types import *

class Analyzer:
    def __init__(self) -> None:
        ... # Nothing to initialise as this is a helper class only.

    # Iterate over each line and traverse the characters
    # until we find a ';' semicolon character which delimits
    # a comment. Remove all following characters
    # Unless the semicolon is in a string. If it is, do nothing.
    def strip_comments(self, lines: list[str]):
        for i, line in enumerate(lines):
            if ';' in line:
                cut_index: any = None
                num_quotes: int = 0
                for j, character in enumerate(line):

                    # Count the number of quotes that we have seen.
                    # If the number is odd then we are in a string,
                    # We dont want to remove part of a string that
                    # just happens to have a semicolon in it.
                    if character == '"':
                        num_quotes += 1

                    elif character == ';':
                        if num_quotes % 2 != 0: # If we are in a string
                            continue

                        # If not.
                        cut_index = j
                        break

                # If there was a comment in the line.
                if cut_index != None:
                    lines[i] = line[0:cut_index].strip()

        return lines

    # Helper function to remove all lines that dont contain
    def remove_blank_lines(self, lines: list[str]):
        blank_characters = [ # Characters that if the line only contains them, remove it.
            '',
            '\n',
            '\r',
            "\r\n",
            "eof",
        ]

        index = 0

        # We use a while loop because when we remove values from the lines list,
        # the for loop doesn't iterate over the same index twice, even if the
        # list is updated.
        while index < len(lines):
            line = lines[index]
            if line in blank_characters:
                lines.pop(index)
                continue

            index += 1

        return lines

    # Helper function to determine whether the param is either a
    # number, a string or a variable.
    def classify_param(self, param: str, is_string):
        # If the value was extracted from a string, the parser will
        # know and can tell us so we dont mistake it for a variable.
        if is_string:
            return String(param)

        if param.isdigit():
            return Number(param)

        return Variable(param)

    # This function converts the raw string form of a line into a broken
    # down array of [line number, operation, param_1, ..., param_n]
    # Converting numbers, variables and string into their respective type.
    def bind_lines(self, lines):
        bound_lines = []

        for line in lines:
            reading_string = False

            # The word simply a string or space delimited string of characters
            # that mean something. i.e: "10"(number) or "var"(operation) or "Hello,
            # World!"(string) op "players"(variable)
            word = ""
            bound_line = [] # The array for the broken down line to be stored in.

            for j, character in enumerate(line):

                match character:
                    case ' ': # Spaces delimit everything other than strings.
                        if reading_string: # If we are reading out a string, simply add the character to the string.
                            word += character
                        else: # If we aren't, finish the word we are reading and start a new one.
                            if word != '':
                                bound_line.append(self.classify_param(word, False))
                                word = ""

                    case '\"': # Quotes delimit strings. If we find one, all following characters until we find another quote is inside of the string.
                        if reading_string:
                            if j > 1: # If the quote proceeds a backslash, then we want the quote literal character not a string delimitation.
                                if line[j - 1] == '\\':
                                    word += '\"'
                                else:
                                    # We want to finish the string and add it to the line.
                                    bound_line.append(self.classify_param(word, True))
                                    word = ""
                                    reading_string = False
                            else:
                                # We want to finish the string and add it to the line.
                                bound_line.append(self.classify_param(word, True))
                                word = ""
                                reading_string = False

                        else:
                            # We want to start reading a string as we just encountered an opening quote.
                            reading_string = True

                    case _:
                        # We haven't encountered a delimiter and thus we just want to add the character to the current word.
                        word += character

            if word != '': # If the word has contents, then add the word to the line.
                bound_line.append(self.classify_param(word, reading_string))

            bound_lines.append(bound_line) # Add the line to the rest of the lines.

        return bound_lines # Return the file for parse to finish the job.

    # Helper function for parsing a raw nob file into a readable and tokenized structure.
    def parse(self, lines):

        lines = self.strip_comments(lines)
        lines = self.remove_blank_lines(lines)
        lines = self.bind_lines(lines)

        parsed_lines = []

        # For each line, separate the params, the operation and the line numbers.
        for params in lines:
            if len(params) < 2: # The line doesn't have an operation.
                print(f"ERROR: There is a line that doesn't have enough parameters.")
                exit()

            # Separate the line number and the operation from the params.
            try:
                line_num = params[0].value
            except:
                # The line doesn't have a line number
                print("ERROR: No line number is present!")
                exit()
            operator = params[1].name

            # Remove the line number and the operation from the params
            params.pop(0); params.pop(0)

            # Add the line number and the operation to the parsed lines and include the variable length params list with it too.
            # line_num: int, operator: str, params: list[str]
            parsed_lines.append((line_num, operator, params))

        return parsed_lines