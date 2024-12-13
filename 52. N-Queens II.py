import copy 

class Solution:
    def __init__(self):
        self.board = []
        self.brain = {}
        self.answer = []
        self.count_queens = 0


    def totalNQueens(self, n: int) -> list[list[str]]:
        if self.board == []:
            self.board = [["." for i in range(n)] for j in range(n)]
        #just loop over all possible starting positions for the first queen!
        self.backtrack(self.board)
        #lets convert the answer to the required format 
        final_answer = []
        for valid_board in self.answer:
            final_board = []
            for row in valid_board:
                final_board.append(''.join(row))
            final_answer.append(final_board)
        return len(final_answer)

    def backtrack(self,board:list[list[str]]) -> None: #possibilities to optimize with memoization
        for i,row in enumerate(board):
            if i!= 0:
                if board[i-1].count('Q') == 0:
                    break 
            for j,element in enumerate(row):
                if element == '.':
                    board[i][j] = 'Q'
                    check = None 
                    first_time = False
                    keyboard = self.board_to_str(board)
                    if keyboard not in self.brain:
                        self.brain[keyboard] = self.isValid(board)
                        check = self.brain[keyboard]
                        first_time = True 
                    if check == True and first_time==True:
                        #print(i,j,board)
                        self.count_queens += 1 
                        self.backtrack(board)
                        if self.count_queens == len(board):
                            if board not in self.answer:
                                board_copy = copy.deepcopy(board)
                                self.answer.append(board_copy)
                            #print("added",board)
                        board[i][j] = '.' 
                        self.count_queens -= 1 
                    else: 
                        board[i][j] = '.'
            
    
    def isValid(self,board:list[list[str]]) -> bool:
        n = len(board)
        columns = [[] for i in range(n)]
        for row in board: 
            if row.count('Q') > 1: 
                return False 
            for j,element in enumerate(row):
                columns[j].append(element)
        for column in columns:
            if column.count('Q') > 1: 
                return False 
        #now that row and column has been loked at. lets look at each queen's diagonal 
        for i,column in enumerate(columns):
            for j,element in enumerate(column):
                if element == 'Q':
                    diagonals = self.get_diagonals((i,j),n)
                    for coordinate in diagonals: 
                        if columns[coordinate[0]][coordinate[1]] == 'Q':
                            return False 
        return True 
        
    def get_diagonals(self, coordinate: tuple,n: int) -> list[tuple]:#outputs list of coordinates in both diagonals 
        diagonals = []
        i = coordinate[0]
        j = coordinate[1]
        while i in range(0,n) and j in range(0,n):#adding top left diagonal 
            if (i,j) != coordinate:
                diagonals.append((i,j))
            i = i-1 
            j = j-1 
        i = coordinate[0]
        j = coordinate[1]
        while i in range(0,n) and j in range(0,n): #adding bottom-right diagonal 
            if (i,j) != coordinate:
                diagonals.append((i,j))
            i = i+1 
            j = j+1 
        i = coordinate[0]
        j = coordinate[1]
        while i in range(0,n) and j in range(0,n): #adding bottom-left diagonal 
            if (i,j) != coordinate:
                diagonals.append((i,j))
            i = i-1
            j = j+1 
        i = coordinate[0]
        j = coordinate[1]
        while i in range(0,n) and j in range(0,n): #adding top-right diagonal 
            if (i,j) != coordinate:
                diagonals.append((i,j))
            i = i+1
            j = j-1 
        return diagonals

    def board_to_str(self, board: list[list[str]]) -> str: 
        ans = ""
        for row in board: 
            ans += ''.join(row)
        return ans 
        
test = Solution()
a = [[".",".","Q",".","."],[".",".",".",".","Q"],[".","Q",".",".","."],[".",".",".","Q","."],["Q",".",".",".","."]]
print(test.isValid(a))
print(test.solveNQueens(4))
#print(len(test.solveNQueens(4)))