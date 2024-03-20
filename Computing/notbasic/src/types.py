class String:
    def __init__(self, value) -> None:
        self.value: str = value

class Integer:
    def __init__(self, value) -> None:
        self.value: int = value

class Variable:
    def __init__(self, name, value) -> None:
        self.name: str = name
        self.value: any = value