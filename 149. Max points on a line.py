import math 

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        max = 1
        brain = {}
        for i,point1 in enumerate(points):
            for j,point2 in enumerate(points):
                if point1 != point2: 
                    tup = self.findTuple(point1,point2)
                    if (point1[0],point1[1],tup) in brain:
                        brain[(point1[0],point1[1],tup)] += 1 
                    else: 
                        brain[(point1[0],point1[1],tup)] = 2
                    if brain[(point1[0],point1[1],tup)] > max: 
                        max = brain[(point1[0],point1[1],tup)]
        return max 
    
    def findTuple(self, p1: list[int], p2: list[int]) -> tuple[int]:
        if p1[1] - p2[1] != 0: 
            m = (p1[0] - p2[0])/(p1[1] - p2[1])
            c = p1[1] - m*p1[0]
        else: 
            m = math.inf
            c = None 
        return (m,c)
    
test = Solution()
testcase = [[1,1],[2,2],[3,3]]
print(test.maxPoints(testcase))