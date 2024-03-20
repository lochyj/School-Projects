import os

class Program:
    def __init__(self) -> None:
        self.operations = []
        self.variables: dict = {}

    def get_variable(self, var, operation):
        if var not in self.variables.keys():
            self.error(f"Variable \"{var}\" not found", operation)

        return self.variables[var]

    def set_variable(self, var, value):
        if var not in self.variables.keys():
            self.variables[var] = value

        self.variables[var] = value

    def error(self, reason, operation):
        print(f"ERROR: {reason}")
        print(f"ERROR ocurred on line {operation.line}")
        exit()

    def get_operation_by_line(self, line_no):
        for operation in self.operations:
            if operation.line == line_no:
                return operation

    def get_next_operation_by_line(self, line_no):
        for i, operation in enumerate(self.operations):
            if operation.line == line_no:
                if i < len(self.operations) - 1:
                    return self.operations[i+1]
                return None

    def run(self):

        # TODO: Sort the operations list from lowest line no. to highest line no.
        running = True

        op = self.operations[0]

        while running:

            if op == None:
                exit()

            jmp = op.execute()

            if jmp != None:
                op = self.get_operation_by_line(jmp)
                continue

            op = self.get_next_operation_by_line(op.line)



class Operation:
    def __init__(self, program) -> None:
        self.line: int = 0
        self.operation: str = ""
        self.params: list[str] = ""
        self.output: any = None
        self.program: Program = program

    def execute(self) -> int | None: # Returns the line number to jump to or
        match self.operation:
            case "print":
                if isinstance(self.params[0], tuple):
                    print(self.params[0][1])
                    return None

                if self.params[0].isdigit():
                    print(param[0])
                    return None

                var_val = self.program.get_variable(self.params[0], self)
                print(var_val)
                return None
            case "add":
                a: int = 0
                b: int = 0
                if self.params[0].isdigit():
                    a = self.params[0]
                else:
                    a = self.program.get_variable(self.params[0], self)

                if self.params[1].isdigit():
                    b = self.params[1]
                else:
                    b = self.program.get_variable(self.params[1], self)

                a = int(a)
                b = int(b)

                self.output = a + b
                return None

            case "sub":
                a: int = 0
                b: int = 0
                if self.params[0].isdigit():
                    a = self.params[0]
                else:
                    a = self.program.get_variable(self.params[0], self)

                if self.params[1].isdigit():
                    b = self.params[1]
                else:
                    b = self.program.get_variable(self.params[1], self)

                a = int(a)
                b = int(b)


                self.output = a - b
                return None

            case "store":
                value = self.program.get_operation_by_line(self.params[0]).output
                self.program.set_variable(self.params[1], value)
                return None

            case "conf":
                try:
                    match self.params[0]:
                        case "width":
                            self.value = os.get_terminal_size()[0]
                        case "height":
                            self.value = os.get_terminal_size()[1]
                        case "os":
                            self.value = os.name
                        case _:
                            self.program.error(f"Unknown config option \"{self.params[0]}\"", self)
                except:
                    self.program.error(f"An unknown error occurred with the operating system", self)
                return None

            case "value":
                value: any = None

                if isinstance(self.params[0], tuple):
                    value = self.params[0][1]
                elif self.params[0].isdigit():
                    value = self.params[0]
                else:
                    value = self.program.get_variable(self.params[0], self)

                self.program.set_variable(self.params[1], self.params[0])
                return None

            case "dec":
                a: int = 0
                if self.params[0].isdigit():
                    a = self.params[0]
                else:
                    a = self.program.get_variable(self.params[0], self)

                a = int(a)
                a -= 1

                self.program.set_variable(self.params[0], a)
                return None

            case "inc":
                a: int = 0
                if self.params[0].isdigit():
                    a = self.params[0]
                else:
                    a = self.program.get_variable(self.params[0], self)

                a = int(a)
                a += 1

                self.program.set_variable(self.params[0], a)
                return None

            case "jnz":
                a: any = None
                if self.params[0].isdigit():
                    a = self.params[0]
                else:
                    a = self.program.get_variable(self.params[0], self)

                a = int(a)

                if a == 0:
                    return None

                return params[1]

            case _:
                self.program.error(f"Unknown operation \"{self.operation}\"", self)

global lines
lines = []

with open("./Computing/notbasic/example.nob", 'r') as file:
    lines = [line.rstrip() for line in file]

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

program = Program()

for line in parsed_lines:
    op = Operation(program)

    op.line = line[0]
    op.operation = line[1]
    op.params = line[2]

    program.operations.append(op)

program.run()
