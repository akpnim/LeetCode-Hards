import statistics 

class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        friends = []
        for j,row in enumerate(grid):
            for i,loc in enumerate(row):
                if loc == 1: 
                    friends.append((i,j))
        x_list = [coor[0] for coor in friends]
        y_list = [coor[1] for coor in friends]
        x_avg = int(statistics.median(x_list))
        y_avg = int(statistics.median(y_list))
        #print(x_avg,y_avg)
        x_dist = 0 
        y_dist = 0 
        for point in friends:
            x_dist += abs(point[0]-x_avg)
            y_dist += abs(point[1]-y_avg)
        #print(friends)
        return x_dist + y_dist
        
test = Solution()
grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,0],[1,1,0,0,0,0,1,0,0],[0,0,0,1,1,1,0,0,0]]
print(test.minTotalDistance(grid))
