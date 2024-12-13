class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        ans = [[0]*len(costs[0])]
        prevmin = 0
        prev2min = 0 
        for i,house in enumerate(costs):
            subans = []
            for j,color in enumerate(house):
                if ans[i][j] == prevmin:
                    subans.append(prev2min+color)
                else: 
                    subans.append(prevmin+color)
            ans.append(subans)
            temp = None 
            prevmin = math.inf 
            prev2min = math.inf 
            for k,ele in enumerate(subans):
                if ele < prevmin: 
                    prevmin = ele 
                    temp = k 
            for k,ele in enumerate(subans):
                if ele < prev2min and k != temp: 
                    prev2min = ele
        return min(ans[-1])