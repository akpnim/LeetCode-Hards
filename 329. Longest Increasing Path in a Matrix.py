class Solution:
    def __init__(self):
        self.brain = {}
        self.matrix = None 
        self.ans = 0

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        self.matrix = matrix 
        for i,row in enumerate(matrix):
            for j,ele in enumerate(row):
                self.brain[(i,j)] = self.dfs((i,j)) 
                if self.brain[(i,j)] > self.ans:
                    self.ans = self.brain[(i,j)]
        #print(self.brain)
        return self.ans + 1 
    
    def dfs(self, coor: tuple[int]) -> int: 
        if coor in self.brain:
            return self.brain[coor]   #check here maybe not possible 
        neighs = self.getNeigh(coor, self.matrix)
        cands = []
        for neigh in neighs:
            if self.matrix[neigh[0]][neigh[1]] > self.matrix[coor[0]][coor[1]]:
                temp = self.dfs(neigh)
                cands.append(temp)
        if cands:
            self.brain[coor] = max(cands) + 1 
        else:
            self.brain[coor] = 0 

        return self.brain[coor]
    
    def getNeigh(self, coor: tuple[int], matrix: list[list[int]]) -> list[tuple[int]]: 
        ans = []
        x = coor[0]
        y = coor[1]
        x_lim = len(matrix) - 1 
        y_lim = len(matrix[0]) - 1 
        if x<x_lim:
            ans.append((x+1,y))
        if x>0:
            ans.append((x-1,y))
        if y<y_lim:
            ans.append((x,y+1))
        if y>0: 
            ans.append((x,y-1))
        return ans 

test = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(test.longestIncreasingPath(matrix))