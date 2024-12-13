#reduced the number of candidates and also improved on the number of cnadidates to consider. 
#(1) try constrained programming to actively further reduce candidates as you move further! 

import time 

time_start = time.time()

class Solution:
    def __init__(self):
        self.candidates = {}
        
    def solveSudoku(self, board: list(list[str])) -> None:

        if self.candidates == {}:
            for i,row in enumerate(board):
                for j,element in enumerate(row):
                    if element == '.':
                        for k in range(1,10):
                            board[i][j] = str(k) 
                            if self.isValid(board) == True: 
                                if (i,j) in self.candidates: 
                                    self.candidates[(i,j)].append(str(k))
                                else: 
                                    self.candidates[(i,j)] = [str(k)]
                            board[i][j] = '.'

        columns = [[] for j in range(9)]
        for i,row in enumerate(board):
            for j,element in enumerate(row):
                columns[j].append(element)

        for i,row in enumerate(board):
            for j,element in enumerate(row):
                if element == '.':
                    for k in self.candidates[(i,j)]:
                        if k not in row[:j] and k not in row[j+1::] and k not in columns[j][:i] and k not in columns[j][i+1::]:
                            board[i][j] = k 
                            if self.isValid(board) == True: 
                                if self.solveSudoku(board) == True:
                                    return True 
                    board[i][j] ='.'
                    return False 
        return True 
                
    def isValid(self, board: list(list[str])) -> bool: 
        default = True 
        boxes = [[] for j in range(9)]
        for i,row in enumerate(board):
            for j,element in enumerate(row):
                    box_index = (i//3)*3 + j//3
                    boxes[box_index].append(element)
        columns = [[] for j in range(9)]
        for i,row in enumerate(board):
            for j,element in enumerate(row):
                columns[j].append(element)
        for i,row in enumerate(board):
            for j,element in enumerate(row):
                if element!= '.':
                    if element in row[:j]: 
                        return False 
                    if element in row[j+1::]: 
                        return False 
                    if element in columns[j][:i]:
                        return False 
                    if element in columns[j][i+1::]:
                        return False 
                    box_index = (i//3)*3 + j//3
                    if boxes[box_index].count(element)>1:
                        return False 
        return default


        
test = Solution()
board = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]

copy = board 
print(test.isValid(board))
c = test.solveSudoku(board)
print(c)
print(board)
d = test.candidates
print(d[(0,0)])

time_end = time.time()
print(time_end-time_start,"s")
