
class SubrectangleQueries:

    def __init__(self, rectangle):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.grid[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]