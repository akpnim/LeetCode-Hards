#KEY IDEA IS STATE TRANSITION IN DP TABLE 
import numpy
class Solution:

    def maxOne(self, prices: list[int]) -> list[int]:
        if prices == []:
            return [0]
        ans = [] 
        maxProfit = 0 
        minVal = prices[0]
        for price in prices: 
            if price< minVal:
                minVal = price 
            if price - minVal > maxProfit:
                maxProfit = price - minVal
            ans.append(maxProfit)
        return ans

    def maxProfit(self, k: int, prices: list[int]) -> int:
        #table = numpy.empty([k+1,len(prices)],dtype=int)
        table = [[None]*len(prices) for i in range(k+1)] #initializing the dp table 
        table[0] = [0]*len(prices) #initializing 
        for i in range(len(table)):#initializing 
            table[i][0] = 0 
        table[1] = self.maxOne(prices) #initializing 
        if len(table) > 2: 
            for kay in range(2,len(table)):
                maxDiff = -prices[0]
                for i in range(1,len(prices)):
                    table[kay][i] = max(table[kay][i-1], prices[i] + maxDiff)
                    maxDiff = max(maxDiff, table[kay-1][i] - prices[i])
        return table[-1][-1]

test = Solution()
k = 4
prices = [1,2,4,2,5,7,2,4,9,0]
print(test.maxProfit(k,prices))
