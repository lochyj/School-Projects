from src.vm import VM
from src.types import *

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

        return None

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
        self.params: list[str] = []

        self.output: any = None

        self.program: Program = program
        self.VM: VM = VM(self, self.program)

    def execute(self) -> int | None: # Returns the line number to jump to or
        match self.operation:
            case "print":
                return self.VM.print()

            case "add":
                return self.VM.add()

            case "sub":
                return self.VM.sub()

            case "mul":
                return self.VM.mul()

            case "div":
                return self.VM.div()

            case "store":
                return self.VM.store()

            case "conf":
                return self.VM.conf()

            case "var":
                return self.VM.var()

            case "inc":
                return self.VM.inc()

            case "dec":
                return self.VM.dec()

            case "jnz":
                return self.VM.jnz()

            case _:
                self.program.error(f"Unknown operation \"{self.operation}\"", self)