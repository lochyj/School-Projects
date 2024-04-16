from src.vm import VM
from src.types import *

class Program:
    def __init__(self) -> None:
        self.operations = []
        self.variables: dict = {}

    def get_variable(self, var, operation):
        if var.name not in self.variables.keys():
            self.error(f"Variable \"{var.name}\" not found", operation)

        return self.variables[var.name]

    def set_variable(self, var, value):
        if var.name not in self.variables.keys():
            self.variables[var.name] = value

        self.variables[var.name] = value

    def error(self, reason, operation):
        print(f"ERROR: {reason}")
        print(f"ERROR ocurred on line {operation.line}")
        exit()

    def get_operation_by_line(self, line_no):
        for operation in self.operations:
            if operation.line == line_no:
                return operation

        return None

    def get_next_operation_by_line(self, line_no):
        for i, operation in enumerate(self.operations):
            if operation.line == line_no:
                if i < len(self.operations) - 1:
                    if self.operations[i+1].line == operation.line:
                        operation.program.error(f"Line {operation.line} has multiple instances", self.operations[i+1])
                        return None
                        # This prevents the user from having multiple
                        # lines of the same number next to each other

                    return self.operations[i+1]
                return None

    def run(self):

        # Sort the lines by number
        heuristic = lambda e: e.line
        self.operations.sort(key=heuristic)

        # TODO: Sort the operations list from lowest line no. to highest line no.
        running = True

        op = self.operations[0]

        while running:

            if op == None:
                exit()

            jmp = op.execute()

            if jmp != None:
                op = self.get_operation_by_line(jmp)

                if op == None:
                    break

                continue
            op = self.get_next_operation_by_line(op.line)
class Operation:
    def __init__(self, program) -> None:
        self.line: int = 0
        self.operation: str = ""
        self.params: list[str] = []

        self.output: any = None

        self.program: Program = program
        self.VM: VM = VM(self, self.program)

    def execute(self) -> int | None: # Returns the line number to jump to or
        self.VM.exec(self.operation)