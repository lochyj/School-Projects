# This is the NoB vm (The NotBasic virtual machine)
import os
import random

from src.types import *

# We create an instance for each operation.
class VM:
    def __init__(self, operation, program) -> None:
        self.operation = operation
        self.program = program

        self.exec = None

    # PRIVATE:

    # Given a type object, convert it to its value
    def get_value(self, object, check_type=None):

        # If the object is a variable, get the value of that variable
        # and recursively call the function again to get the actual value
        if self.assert_type(object, Variable):
            return self.get_value(self.program.get_variable(object, self.operation), check_type=check_type)
            # Return it once we've found it...

        # If we are checking the type, assert that it is the given type
        if check_type != None:
            if not self.assert_type(object, check_type):
                return None # If not, return None to enable us to check it later.

        # Now actually return the value of the object
        return object.value

    # Simple helper function that probably isn't needed.
    def assert_type(self, object, type):
        # If the object isn't an instance of the specified type
        if not isinstance(object, type):
            return False

        return True

    # PUB:

    def print(self):
        # Format:
        # <line_no> print <param>

        param = self.operation.params[0]

        if len(self.operation.params) > 1:
            # TODO: Throw warning
            ...

        value = self.get_value(param)
        print(str(value).replace("\\n", '\n'), end='')
        return None

    def println(self):
        # Format:
        # <line_no> println <param>

        param = self.operation.params[0]

        if len(self.operation.params) > 1:
            # TODO: Throw warning
            ...

        value = self.get_value(param)
        print(str(value).replace("\\n", '\n'))
        return None

    def add(self):
        # Format:
        # <line_no> add <param1> <param2>
        # -> <param1> + <param2>

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if self.assert_type(param1, String) or self.assert_type(param2, String):
            self.program.error("Cannot add Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot add Strings", self.operation)

        self.operation.output = Integer(a + b)
        return None

    def sub(self):
        # Format:
        # <line_no> sub <param1> <param2>
        # -> <param1> - <param2>

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if self.assert_type(param1, String) or self.assert_type(param2, String):
            self.program.error("Cannot subtract Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot subtract Strings", self.operation)

        self.operation.output = Integer(a - b)
        return None

    def mul(self):
        # Format:
        # <line_no> mul <param1> <param2>
        # -> <param1> * <param2>

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if self.assert_type(param1, String) or self.assert_type(param2, String):
            self.program.error("Cannot multiply Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot multiply Strings", self.operation)

        self.operation.output = Integer(a * b)
        return None

    def div(self):
        # Format:
        # <line_no> div <param1> <param2>
        # -> <param1> / <param2>

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if self.assert_type(param1, String) or self.assert_type(param2, String):
            self.program.error("Cannot multiply Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot multiply Strings", self.operation)

        if b == 0:
            self.program.error("Cannot divide a number by 0", self.operation)

        self.operation.output = Integer(a / b)
        return None

    def store(self):
        # Format:
        # <line_no> store <param1> <param2>
        # -> <param2> = <param1> (var = line_num.output)

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        param1_value = self.get_value(param1, check_type=Integer)

        if param1_value == None:
            self.program.error("Line number must be an integer type", self.operation)

        value = self.program.get_operation_by_line(param1_value)

        if value == None:
            self.program.error(f"Line {param1_value} does't exist", self.operation)

        self.program.set_variable(param2, value.output)

    def conf(self):
        # Format:
        # <line_no> conf <param1>

        param = self.operation.params[0].value
        try:
            match param:
                case "width":
                    self.operation.output = Integer(os.get_terminal_size()[0])
                case "height":
                    self.operation.output = Integer(os.get_terminal_size()[1])
                case "os":
                    self.operation.output = String(os.name)
                case _:
                    self.program.error(f"Unknown config option \"{param}\"", self.operation)
        except:
            self.program.error(f"An unknown error occurred with the operating system or operating environment", self.operation)

        return None

    def var(self):
        # Format:
        # <line_no> store <param1> <param2>
        # -> <param1> = <param2> (var = value)

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        if not self.assert_type(param1, Variable):
            self.program.error("Cannot set the value of a non variable", self.operation)

        self.program.set_variable(param1, param2)
        return None

    def dec(self):
        # Format:
        # <line_no> dec <param1>
        # -> <param1>--

        param1 = self.operation.params[0]

        if self.assert_type(param1, String):
            self.program.error("Cannot decrease a Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)

        if a == None:
            self.program.error("Cannot decrease a String", self.operation)

        self.operation.output = Integer(a - 1)
        return None

    def inc(self):
        # Format:
        # <line_no> inc <param1>
        # -> <param1>++

        param1 = self.operation.params[0]

        if self.assert_type(param1, String):
            self.program.error("Cannot increase a Strings", self.operation)

        a = self.get_value(param1, check_type=Integer)

        if a == None:
            self.program.error("Cannot increase a String", self.operation)

        self.operation.output = Integer(a + 1)
        return None

    def jnz(self):
        # Format:
        # <line_no> jnz <param1> <param2>
        # <param1> -> var/num to compare
        # <param2> -> line number

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        p2_val = self.get_value(param2, check_type=Integer)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot compare a String", self.operation)

        # If a is equal to 0, then we dont need to jump anywhere, continue onwards!
        if a == 0:
            return None

        if self.program.get_operation_by_line(b) == None:
            self.program.error(f"Line {param2} cannot be found", self.operation)

        return p2_val

    def jz(self):
        # Format:
        # <line_no> jz <param1> <param2>
        # <param1> -> var/num to compare
        # <param2> -> line number

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        p2_val = self.get_value(param2, check_type=Integer)

        a = self.get_value(param1, check_type=Integer)
        b = self.get_value(param2, check_type=Integer)

        if a == None or b == None:
            self.program.error("Cannot compare a String", self.operation)

        # If a doesn't equal to 0, then we dont need to jump anywhere, continue onwards!
        if a != 0:
            return None

        if self.program.get_operation_by_line(b) == None:
            self.program.error(f"Line {param2} cannot be found", self.operation)

        return p2_val

    def jmp(self):
        # Format:
        # <line_no> jmp <param1>
        # <param1> -> line number

        if len(self.operation.params) != 2:
            ... # TODO: Throw warning or error.

        param1 = self.operation.params[0]

        value = self.get_value(param1, check_type=Integer)

        if value == None:
            self.program.error("Cannot jump to a String", self.operation)

        if self.program.get_operation_by_line(value) == None:
            self.program.error(f"Line {value} cannot be found", self.operation)

        return value

    def cat(self):
        # Format:
        # <line_no> cat <param1> <param2>

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        str1 = self.get_value(param1, check_type=String)
        str2 = self.get_value(param2, check_type=String)

        if str1 == None or str2 == None:
            self.program.error("Cannot concatenate non-strings", self.operation)

        self.operation.output = String(str1 + str2)

        return None

    def rand(self):
        # Format:
        # <line_no> rand <param1> <param2>
        # <param1> -> Min value
        # <param2> -> Max value

        param1 = self.operation.params[0]
        param2 = self.operation.params[1]

        mn = self.get_value(param1, check_type=Integer)
        mx = self.get_value(param2, check_type=Integer)

        if mn == None or mx == None:
            self.program.error("Cannot use strings as random range", self.operation)

        self.operation.output = Integer(random.randint(mn, mx))
        return None
