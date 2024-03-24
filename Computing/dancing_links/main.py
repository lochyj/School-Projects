
# The general principal behind dancing links is as follows:
# L[x] ~ The pointer to the element on the left of element x (still contained within the x element data structure)
# R[x] ~ The pointer to the element on the right of element x (still contained within the x element data structure)
# L[R[x]] ~ The the pointer to the element that element R[x] points to, which is on its left.
# R[L[x]] ~ The the pointer to the element that element L[x] points to, which is on its right.
# L[R[x]] <- L[x] ~ Replace the pointer of L[R[x]] to point to the element to the left of element x
# R[L[x]] <- R[x] ~ Replace the pointer of R[L[x]] to point to the element to the right of element x
# 2a.) L[R[x]] <- x ~ Replace the pointer of L[R[x]] to point to element x
# 2b.) R[L[x]] <- x ~ Replace the pointer of R[L[x]] to point to element x
# 2a and 2b work because we dont remove x from the list and it just
# sits in purgatory. In theory we could free x but in many cases it
# would sit between memory addr(L[x] + sizeof(L[x])) and addr(R[x]).
# Unless sizeof(x) is a page large and is page aligned, forget it...
# Another option would be to shift all elements over but this is really
# compute intensive and wastes precious cpu cycles :)

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


# --------|
# Classes |
# --------|

class Header:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.up = None
        self.down = None

class Element:
    def __init__(self) -> None:
        self.header: Header = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None

class Matrix:
    def __init__(self, rows, columns) -> None:
        self.width = columns
        self.height = rows

        self.headers: list[Header] = [Header() for _ in range(self.width)]
        self.matrix: list[list[Element]] = [[Element() for _ in range(self.height)] for _ in range(self.width)]

        self.base_header: Header = Header()

        self.base_header.down = None
        self.base_header.up = None
        self.base_header.left = self.headers[len(self.headers) - 1] # Assumes that the width is > 0
        self.base_header.right = self.headers[0]

        # No comments good luck :)

        for row in range(rows):
            for col in range(columns):

                l: Element = None
                r: Element = None
                u: Element | Header = self.headers[col]
                d: Element | Header = self.headers[col]

                if row != 0 and row != self.width:
                    u = self.matrix[col][row - 1]

                if row <= rows - 2:
                    d = self.matrix[col][row + 1]

                if col != 0:
                    l = self.matrix[col - 1][row]

                if col <= columns - 2:
                    r = self.matrix[col + 1][row]

                el: Element = self.matrix[col][row]
                el.left = l
                el.right = r
                el.up = u
                el.down = d

                if isinstance(u, Header):
                    u.down = el

                if isinstance(d, Header):
                    d.up = el

                el.header = self.headers[col]

                self.matrix[col][row] = el

        for i, header in enumerate(self.headers):
            if i == 0:
                header.left = self.base_header
            else:
                header.left = self.headers[i - 1]

            if i == len(self.headers) - 1:
                header.right = self.base_header
            else:
                header.right = self.headers[i + 1]

class Solver:
    def __init__(self) -> None:
        self.matrix = Matrix(1568, 72)

    def create_matrix():
        # See generate_matrix.py
        ...


# -----|
# Init |
# -----|

matrix = Matrix(1568, 72)

headers = matrix.headers

# The first 12 columns of the matrix are for each of the 12 pentominoes.
F = matrix.matrix[0]
I = matrix.matrix[1]
L = matrix.matrix[2]
P = matrix.matrix[3]
N = matrix.matrix[4]
T = matrix.matrix[5]
U = matrix.matrix[6]
V = matrix.matrix[7]
W = matrix.matrix[8]
X = matrix.matrix[9]
Y = matrix.matrix[10]
Z = matrix.matrix[11]

print(matrix.base_header.left.down) # Works!