import sys

from src.parse import Analyzer
from src.execute import Program, Operation
from src.input import get_user_in

# Helper function to read in the lines of a file as a list of strings
def open_file(file_path):
    lines = []

    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]

    return lines

def main():
    # Initialise the required classes
    program = Program() # The main storage class of the program
    analyzer = Analyzer() # A helper class for converting the raw file into operable chunks

    file: any = None

    # Open the file provided by the user.
    # Or alternatively, if there is no file or the file doesn't
    # exist, get the user to input the program manually.
    try:
        file = open_file(sys.argv[1])
    except:
        file = get_user_in()

    # Parse and tokenize the lines into a useable format
    parsed_lines = analyzer.parse(file)

    # Format the program into a list of operations
    for line in parsed_lines:
        op = Operation(program)

        op.line = line[0]
        op.operation = line[1]
        op.params = line[2]

        program.operations.append(op) # Add them to the program

    # Run the operations that we created above.
    program.run()

# Run the program!
if __name__ == "__main__":
    main()