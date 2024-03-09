
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

class Element:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.value = None



class Matrix:
    def __init__(self, columns, rows) -> None:
        self.width = columns
        self.height = rows

        self.matrix: list[list[Element]] = [[Element() for _ in range(self.width)] for _ in range(self.height)]

        for row in range(rows):
            for col in range(columns):
                l: Element | None = None
                r: Element | None = None
                u: Element | None = None
                d: Element | None = None

                if row != 0 and row != self.width:
                    u = self.matrix[row - 1][col]

                if row <= rows - 2:
                    d = self.matrix[row + 1][col]

                if col != 0:
                    l = self.matrix[row][col - 1]

                if col <= columns - 2:
                    r = self.matrix[row][col + 1]

                el: Element = self.matrix[row][col]
                el.left = l
                el.right = r
                el.up = u
                el.down = d

                self.matrix[row][col] = el

matrix = Matrix(5, 3)

el = matrix.matrix[0][0]

print(el.left) # -> None
print(el.right) # -> Element
print(el.right.right) # -> Element
print(el.right.right.right) # -> Element
print(el.right.right.right.right) # -> Element
print(el.right.right.right.right.right) # -> None
