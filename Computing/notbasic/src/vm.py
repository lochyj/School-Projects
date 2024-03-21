# This is the NoB vm (The NotBasic virtual machine)
import os

from src.types import *

# We create an instance for each operation.
class VM:
    def __init__(self, operation, program) -> None:
        self.operation = operation
        self.program = program

        self.exec = None

    def print(self):
        param = self.operation.params[0]

        if len(self.operation.params) > 1:
            # TODO: Throw warning
            ...

        if isinstance(param, String) or isinstance(param, Integer):
            print(str(param.value).replace("\\n", '\n'))
            return None

        var_val = self.program.get_variable(param.name, self.operation)
        print(str(var_val.value).replace("\\n", '\n'))
        return None

    def add(self):

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if isinstance(param1, String) or isinstance(param2, String):
            self.program.error("Cannot add Strings", self.operation)

        a: int = 0
        b: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot add Strings", self.operation)
            a = a.value

        if isinstance(param2, Integer):
            b = param2.value
        else:
            b = self.program.get_variable(param2.name, self)
            if isinstance(b, String):
                self.program.error("Cannot add Strings", self.operation)
            b = b.value

        if isinstance(a, String) or isinstance(b, String):
            self.program.error("Cannot add Strings", self.operation)

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
            b = int(b)
        except:
            ...

        self.operation.output = Integer(a + b)
        return None

    def sub(self):

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if isinstance(param1, String) or isinstance(param2, String):
            self.program.error("Cannot subtract Strings", self.operation)

        a: int = 0
        b: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot subtract Strings", self.operation)
            a = a.value

        if isinstance(param2, Integer):
            b = param2.value
        else:
            b = self.program.get_variable(param2.name, self)
            if isinstance(b, String):
                self.program.error("Cannot subtract Strings", self.operation)
            b = b.value

        if isinstance(a, String) or isinstance(b, String):
            self.program.error("Cannot subtract Strings", self.operation)

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
            b = int(b)
        except:
            ...

        self.operation.output = Integer(a - b)
        return None

    def mul(self):

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if isinstance(param1, String) or isinstance(param2, String):
            self.program.error("Cannot subtract Strings", self.operation)

        a: int = 0
        b: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot subtract Strings", self.operation)
            a = a.value

        if isinstance(param2, Integer):
            b = param2.value
        else:
            b = self.program.get_variable(param2.name, self)
            if isinstance(b, String):
                self.program.error("Cannot subtract Strings", self.operation)
            b = b.value

        if isinstance(a, String) or isinstance(b, String):
            self.program.error("Cannot subtract Strings", self.operation)

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
            b = int(b)
        except:
            ...

        self.operation.output = Integer(a * b)
        return None

    def div(self):

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if isinstance(param1, String) or isinstance(param2, String):
            self.program.error("Cannot subtract Strings", self.operation)

        a: int = 0
        b: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot subtract Strings", self.operation)
            a = a.value

        if isinstance(param2, Integer):
            b = param2.value
        else:
            b = self.program.get_variable(param2.name, self)
            if isinstance(b, String):
                self.program.error("Cannot subtract Strings", self.operation)
            b = b.value

        if isinstance(a, String) or isinstance(b, String):
            self.program.error("Cannot subtract Strings", self.operation)

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
            b = int(b)
        except:
            ...

        if b == 0:
            self.program.error("Cannot divide a number by 0", self.operation)

        self.operation.output = Integer(a / b)
        return None

    def store(self):

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        value = self.program.get_operation_by_line(param1.value)

        if value == None:
            self.program.error(f"Line {param1} does't exist", self.operation)

        self.program.set_variable(param2.name, value.output)

    def conf(self):
        param = self.operation.params[0].value
        try:
            match param:
                case "width":
                    self.value = os.get_terminal_size()[0]
                case "height":
                    self.value = os.get_terminal_size()[1]
                case "os":
                    self.value = os.name
                case _:
                    self.program.error(f"Unknown config option \"{param}\"", self.operation)
        except:
            self.program.error(f"An unknown error occurred with the operating system or operating environment", self.operation)
        return None

    def var(self):

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        name = param1
        value: any = None

        if isinstance(param2, Variable):
            value = self.program.get_variable(param2.name, self)
        else:
            value = param2

        if isinstance(param1, Variable):
            name = param1.name

        self.program.set_variable(name, value)
        return None

    def dec(self):

        if len(self.operation.params) != 1:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]

        if isinstance(param1, String):
            self.program.error("Cannot decrease a String", self.operation)

        a: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot decrease a String", self.operation)
            a = a.value

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
        except:
            ...

        self.operation.output = Integer(a - 1)
        return None

    def inc(self):

        if len(self.operation.params) != 1:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]

        if isinstance(param1, String):
            self.program.error("Cannot increase a String", self.operation)

        a: int = 0
        if isinstance(param1, Integer):
            a = param1.value
        else:
            a = self.program.get_variable(param1.name, self)
            if isinstance(a, String):
                self.program.error("Cannot increase a String", self.operation)
            a = a.value

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
        except:
            ...

        self.operation.output = Integer(a + 1)
        return None

    def jnz(self):

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if isinstance(param1, String):
            self.program.error("Cannot compare a String", self.operation)

        a: any = None
        if isinstance(param1, Variable):
            a = self.program.get_variable(param1.name, self)

            if isinstance(a, String):
                self.program.error("Cannot compare a String", self.operation)

            a = a.value

        else:
            a = param1.value

        # Just to be sure. TODO: Verify that we don't need this...
        try:
            a = int(a)
        except:
            ...

        # If a is equal to 0, then we dont need to jump anywhere, continue onwards!
        if a == 0:
            return None

        if not isinstance(param2, Integer) or self.program.get_operation_by_line(param2.value) == None:
            self.program.error(f"Line {param2} cannot be found", self.operation)

        return param2.value
