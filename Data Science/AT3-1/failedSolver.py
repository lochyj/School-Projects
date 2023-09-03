
# So we dont have a linked grid
def copyGrid(grid):
    new_grid = []

    for row in grid:
        new_grid.append(row.copy())

    return new_grid

def isValidMove(board, direction):
    blank_row, blank_col = None, None

    # Find the current position of the blank (0) cell
    for i in range(4):
        for j in range(4):
            if board[i][j] == BLANK_CELL:
                blank_row, blank_col = i, j

    # Check if the move is valid based on the direction
    if direction == 'u':
        return blank_row > 0
    elif direction == 'd':
        return blank_row < 3
    elif direction == 'l':
        return blank_col > 0
    elif direction == 'r':
        return blank_col < 3
    else:
        return False  # Invalid direction

def makeMove(board, direction):

    if isValidMove(board, direction) == False:
        return None

    blank_row, blank_col = None, None

    # Find the current position of the blank (0) cell
    for i in range(CELLS_WIDE):
        for j in range(CELLS_HIGH):
            if board[i][j] == BLANK_CELL:
                blank_row, blank_col = i, j

    # Check if the move is valid
    if direction == 'u':
        board[blank_row][blank_col], board[blank_row - 1][blank_col] = board[blank_row - 1][blank_col], board[blank_row][blank_col]
        return board
    elif direction == 'd':
        board[blank_row][blank_col], board[blank_row + 1][blank_col] = board[blank_row + 1][blank_col], board[blank_row][blank_col]
        return board
    elif direction == 'l':
        board[blank_row][blank_col], board[blank_row][blank_col - 1] = board[blank_row][blank_col - 1], board[blank_row][blank_col]
        return board
    elif direction == 'r':
        board[blank_row][blank_col], board[blank_row][blank_col + 1] = board[blank_row][blank_col + 1], board[blank_row][blank_col]
        return board


def manhattan_distance(board):
    distance = 0

    for i in range(CELLS_WIDE):
        for j in range(CELLS_HIGH):
            if board[i][j] != BLANK_CELL:
                destPos = ((board[i][j] - 1) // CELLS_WIDE,
                                (board[i][j] - 1) % CELLS_HIGH)
                distance += abs(destPos[0] - i)
                distance += abs(destPos[1] - j)

    return distance

def findNextMove(grid):
    best_move = ''
    best_score = -9999999999

    moves = ['u', 'd', 'l', 'r']

    move_scores = [0, 0, 0, 0]

    for move in moves:

        temp_grid = copyGrid(gameGrid)

        temp_grid = makeMove(temp_grid, move)

        if temp_grid == None:
            continue

        score = manhattan_distance(grid)

        print(f"Move: {move}, Score: {score}")

        if score > best_score:
            best_score = score
            best_move = move

        move_scores.append(score)

    # if all of the scores are the same, just return a random move
    if all(score == best_score for score in move_scores):
        return random.choice(moves)

    temp_grid = copyGrid(gameGrid)

    if makeMove(temp_grid, best_move) == None:
        return random.choice(moves.remove(best_move))

    return best_move
