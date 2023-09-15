
def DFS_generate_maze(full_maze: list[list[list[int]]]) -> list[list[list[int]]]:
    ...

def generate_maze(width: int, height: int) -> list[list[list[int]]]:
    # [a, b]
    maze = [[[0, 0] for _ in range(width)] for _ in range(height)]

    print(*maze)

    maze = DFS_generate_maze(maze)

    return maze

_ = generate_maze(5, 5)