class String:
    def __init__(self, value) -> None:
        self.value: str = value

class Integer:
    def __init__(self, value) -> None:
        self.value: int = float(value)

class Variable:
    def __init__(self, name) -> None:
        self.name: str = name