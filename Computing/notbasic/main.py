from src.parse import parse
from src.execute import Program, Operation

def main():

    program = Program()

    parsed_lines = parse("./Computing/notbasic/test.nob")

    for line in parsed_lines:
        op = Operation(program)

        op.line = line[0]
        op.operation = line[1]
        op.params = line[2]

        program.operations.append(op)

    program.run()

if __name__ == "__main__":
    main()