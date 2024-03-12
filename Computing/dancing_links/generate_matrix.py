# ------------|
# Pentominoes |
# ------------|

U = [
    "##",
    "#", # U
    "##"
]

X = [
    " #",
    "###", # X
    " #"
]

Y = [
    " #",
    "####" # Y
]

I = [
    "#####" # I
]

P = [
    "###", # P
    " ##"
]

V = [
    "###",
    "  #", # V
    "  #"
]

T = [
    "###",
    " #", # T
    " #"
]

N = [
    "##",
    " ###" # N
]

W = [
    " ##",
    "##", # W
    "#"
]

L = [
    "####", # L
    "#"
]

Z = [
    "#",
    "###", # Z
    "  #"
]

F = [
    " #",
    "###", # F
    "  #"
]

def get_pentomino(pentomino, rotation):
    ...

class MiniMatrix:
    def __init__(self, width: int, height: int) -> None:
        self.matrix: list[list[int]] = [[0 for _ in range(height)] for _ in range(width)]

def main():
    with open("./matrix.txt", "w") as file:
        ...


if __name__ == "__main__":
    main()