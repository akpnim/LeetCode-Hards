import heapq
class Solution: 
    def trapRainWater(self, heightMap: list[list[int]]) -> int: 
        #Step 1: adding all the boundaries to the heap 
        visited = set()
        heap = []
        total = 0 
        heapq.heapify(heap)
        for i,row in enumerate(heightMap):
            for j,val in enumerate(row):
                if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[0])-1: 
                    heapq.heappush(heap, [val,i,j])
                    visited.add((i,j))

        while heap: 
            curr = heapq.heappop(heap)
            neighs = self.getNeigh((curr[1],curr[2]),heightMap)
            for neigh in neighs:
                if neigh not in visited: 
                    total += max(0, curr[0]-heightMap[neigh[0]][neigh[1]])
                    heapq.heappush(heap,[max(curr[0],heightMap[neigh[0]][neigh[1]]), neigh[0],neigh[1]])
                    visited.add(neigh)
        return total         


    def getNeigh(self, coor: tuple[int], heightMap: list[list[int]]) -> int: 
        x_lim = len(heightMap) - 1 
        y_lim = len(heightMap[0]) - 1 
        x,y = coor[0],coor[1]
        ans = []
        if x < x_lim:
            ans.append((x+1,y))
        if x > 0: 
            ans.append((x-1,y))
        if y < y_lim:
            ans.append((x,y+1))
        if y > 0: 
            ans.append((x,y-1))
        return ans 


test = Solution()
heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
print(test.trapRainWater(heightMap))