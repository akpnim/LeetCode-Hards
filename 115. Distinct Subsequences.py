#Solved using 2D - dynamic table/array 

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0 
        #let's initialize the 2D array 
        table = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        for i,chart in enumerate(t):
            for j,chars in enumerate(s):
                if chart == chars and j>=i:
                    if i+1 == 1: 
                        table[i+1][j+1] = table[i+1][j] + 1 
                    else: 
                        table[i+1][j+1] = table[i][j] + table[i+1][j]
                else: 
                    table[i+1][j+1] = table[i+1][j]
        return table[len(t)][len(s)]
        

#facing problem due to string concat
test = Solution()
s = "rabbbit"
t = "rabbit"
print(test.numDistinct(s,t))