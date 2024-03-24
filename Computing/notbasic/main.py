import sys

from src.parse import Analyzer
from src.execute import Program, Operation
from src.input import get_user_in

def open_file(file_path):
    lines = []

    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]

    return lines

def main():
    program = Program()
    analyzer = Analyzer()

    file: any = None

    try:
        # TODO: use argparse instead
        file = open_file(sys.argv[1])
    except:
        file = get_user_in()

    parsed_lines = analyzer.parse(file)

    for line in parsed_lines:
        op = Operation(program)

        op.line = line[0]
        op.operation = line[1]
        op.params = line[2]

        program.operations.append(op)

    program.run()

if __name__ == "__main__":
    main()