from src.vm import VM
from src.types import *

class Program:
    def __init__(self) -> None:
        self.operations = []
        self.variables: dict = {}

    # Helper function to get the value of a variable with the given name
    def get_variable(self, var, operation):
        if var.name not in self.variables.keys():
            self.error(f"Variable \"{var.name}\" not found", operation)

        return self.variables[var.name]

    # Helper function to set the value of a variable with the given name
    def set_variable(self, var, value):
        if var.name not in self.variables.keys():
            self.variables[var.name] = value

        self.variables[var.name] = value

    # Helper function for when the program fails in an unrecoverable way
    def error(self, reason, operation):
        print(f"ERROR: {reason}")
        print(f"ERROR ocurred on line {operation.line}")
        exit()

    # Given a line number, return the operation at the line if any.
    def get_operation_by_line(self, line_no):
        for operation in self.operations:
            if operation.line == line_no:
                return operation

        return None

    # Given a line number, return the next operation if there is any.
    def get_next_operation_by_line(self, line_no):
        # Iterate over each operation and find the operation that line_no corresponds to.
        for i, operation in enumerate(self.operations):
            if operation.line == line_no:
                if i < len(self.operations) - 1:

                    # If it isnt the last operation then go one operation ahead and return it.
                    if self.operations[i+1].line == operation.line:

                        operation.program.error(f"Line {operation.line} has multiple instances", self.operations[i+1])
                        return None
                        # This prevents the user from having multiple
                        # lines of the same number next to each other - confusing the interpreter.

                    return self.operations[i+1]
                return None

    def run(self):

        # Sort the lines by number
        # the sorting heuristic that determines what the value of each element is for sort to order them.
        heuristic = lambda e: e.line
        self.operations.sort(key=heuristic)

        running = True
        current_operation = self.operations[0] # Start the program.

        try:
            while running:

                if current_operation == None:
                    exit()

                jump_code = current_operation.execute()

                if jump_code != None: # If the operation returned a line number to jump to...
                    current_operation = self.get_operation_by_line(jump_code) # Jump to it
                else:
                    current_operation = self.get_next_operation_by_line(current_operation.line) # Else just get the next operation

        except KeyboardInterrupt: # Handle keyboard interrupts. I.E: Ctrl+c to stop the process.
            print("Program finished early because the user stopped the process with a keyboard interrupt.")
            exit()

# The operation data class.
# This stores all important information for each operation.
class Operation:
    def __init__(self, program) -> None:
        # Operation declaration and additional information.
        self.line: int = 0
        self.operation: str = ""
        self.params: list[str] = []

        self.output: any = None # For operations like `store` to access and and operations like `add` to address

        # Class instances that are needed for the operation to be performed.
        self.program: Program = program
        self.VM: VM = VM(self, self.program)

    # Wrapper function for executing the operation that the operation class instance declares.
    def execute(self) -> int | None: # Returns the line number to jump to or
        return self.VM.exec(self.operation)