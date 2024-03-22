class String:
    def __init__(self, value) -> None:
        self.value: str = value

class Integer:
    def __init__(self, value) -> None:
        if isinstance(value, int):
            print(value)
            self.value: int = value
        else:
            self.value: int = int(value)

class Variable:
    def __init__(self, name) -> None:
        self.name: str = name