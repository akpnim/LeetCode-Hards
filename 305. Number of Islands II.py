"""
Very good question - have to implement a custom Union-Find structure using a ditionary and co-ordinates. Great exercise to 
essentially practice nuances of Union-Find structure such as path compression and ranking roots. Basically initialize 
with each coor's root as itself and also each coor's rank as 0.
"""

class Solution:
    def __init__(self):
        self.parent = None #[i for i in range(n)]
        self.rank = None #[0 for 0 in range(n)] 
        self.mydict = {}
        self.visited = set()

    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        self.parent = [i for i in range(len(positions))]
        self.rank = [0 for i in range(len(positions))]
        for i,coor in enumerate(positions):
            self.mydict[(coor[0],coor[1])] = i
        grid = [['0' for i in range(n)] for j in range (m)]
        ans = []
        mergecount = 0 
        unicount = 0 
        for z,coor in enumerate(positions): 
            if (coor[0],coor[1]) not in self.visited: 
                unicount += 1 
                grid[coor[0]][coor[1]] = '1'
                neighs = self.getNeigh(m,n,coor)
                for neigh in neighs:
                    if grid[neigh[0]][neigh[1]] == '1' and not self.Connected(self.mydict[(neigh[0],neigh[1])],self.mydict[(coor[0],coor[1])]):
                        self.Union(self.mydict[(neigh[0],neigh[1])],self.mydict[(coor[0],coor[1])])
                        mergecount+=1 
                self.visited.add((coor[0],coor[1]))
            ans.append(unicount-mergecount)
        return ans 
    
    def Union(self, x: int, y: int):
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        xRank = self.rank[xRoot]
        yRank = self.rank[yRoot]
        if xRank > yRank: 
            self.parent[yRoot] = xRoot
        elif yRank > xRank: 
            self.parent[xRoot] = yRoot 
        elif xRank == yRank: 
            self.parent[xRoot] = yRoot 
            self.rank[yRoot] += 1 #only one case where the rank is incremented 

    
    def Connected(self, x: int, y: int) -> bool: 
        return self.Find(x) == self.Find(y) 
    
    def Find(self, x:int) -> int: 
        if self.parent[x] != x: 
            self.parent[x] = self.Find(self.parent[x]) #path compression 
        return self.parent[x]
    
    def getNeigh(self, m:int, n: int, coor: list[int]) -> list[list[int]]:
        xlim = m-1
        ylim = n-1 
        x = coor[0]
        y = coor[1]
        ans = []
        if x+1 <= xlim: 
            ans.append([x+1,y])
        if x-1 >= 0:
            ans.append([x-1,y])
        if y+1 <= ylim:
            ans.append([x,y+1])
        if y-1 >= 0: 
            ans.append([x,y-1])
        return ans 