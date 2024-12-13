from collections import deque
class Solution:
    def __init__(self):
        self.totals = {}
        self.friends = 0 

    def shortestDistance(self, grid: list[list[int]]) -> int:
        for row in grid: 
            for square in row: 
                if square == 1: 
                    self.friends += 1 
        
        for i,row in enumerate(grid):
            for j,square in enumerate(row):
                if square == 1: 
                    self.calcBFS((i,j),grid)
        
        candidates = []
        
        for coor in self.totals: 
            if len(self.totals[coor]) == self.friends:
                candidates.append(sum(self.totals[coor]))
        
        if candidates:
            return min(candidates)
        
        else: 
            return -1 
    
    def calcBFS(self, coor: tuple[int], grid: list[list[int]]):
        total = 0 
        friends = 1 
        visited = set()
        queue = deque([[coor,0]])
        visited.add(coor)
        while queue: 
            cur = queue.popleft()
            if grid[cur[0][0]][cur[0][1]] == 0:
                if cur[0] in self.totals:
                    self.totals[cur[0]].append(cur[1])
                else: 
                    self.totals[cur[0]] = [cur[1]]

            neighs = self.getNeigh(cur[0],grid)
        
            for neigh in neighs: 
                if neigh not in visited: 
                    if grid[neigh[0]][neigh[1]] == 0:
                        queue.append([neigh,cur[1]+1])
                        visited.add(neigh)

   
    
    def getNeigh(self, cur: tuple[int], grid: list[list[int]]) -> list[tuple[int]]:
        m = len(grid) -1 
        n = len(grid[0]) -1 
        x = cur[0]
        y = cur[1]
        ans = [] 
        if x> 0: 
            ans.append((x-1,y))
        if x<m: 
            ans.append((x+1, y))
        if y > 0: 
            ans.append((x,y-1))
        if y<n: 
            ans.append((x,y+1))
        return ans 

test = Solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(test.shortestDistance(grid))