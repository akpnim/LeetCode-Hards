class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix 
        self.cumul = []
        for row in matrix: 
            to_add = []
            running = 0 
            for i,ele in enumerate(row):
                running += ele 
                to_add.append(running)
            self.cumul.append(to_add)
        

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val 
        to_update = self.matrix[row]
        to_add = []
        running = 0
        for i,ele in enumerate(to_update):
            running += ele 
            to_add.append(running)
        self.cumul[row] = to_add


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = 0 
        b = 0 
        c = 0 
        if row1 > 0 and col1 > 0: 
            c = self.total(row1-1,col1-1)
        if row1 > 0: 
            a = self.total(row1-1,col2)
        if col1 > 0: 
            b = self.total(row2,col1-1)
        tot = self.total(row2,col2)
        return tot - a - b + c 
    
    def total(self, row:int, col: int) -> int: 
        tot = 0
        for i in range(row+1):
            tot += self.cumul[i][col]
        return tot 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)