# Simple classes to store string, number and variable information.

class String:
    def __init__(self, value) -> None:
        self.value: str = value

class Number:
    def __init__(self, value) -> None:
        self.value: int = float(value)

class Variable:
    def __init__(self, name) -> None:
        self.name: str = name # The name is used to access the value at runtime.
        # The value of the variable is stored in the program class.