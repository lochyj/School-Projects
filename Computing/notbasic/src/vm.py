# This is the NoB vm (The NotBasic virtual machine)


# We create an instance for each operation.
class VM:
    def __init__(self, operation, program) -> None:
        self.operation = operation
        self.program = program

        self.exec = None

    def print(self):
        ...

    def add(self):
        ...

    def sub(self):
        ...

    def store(self):
        ...

    def conf(self):
        ...

    def value(self):
        ...

    def dec(self):
        ...

    def inc(self):
        ...

    def jnz(self):
        ...
