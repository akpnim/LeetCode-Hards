#This solution below worked! Memoization hurts memory and speed! - figure out why. 
import math 
class Solution:
    def __init__(self):
        self.brain = {}

    def minCut(self, s: str) -> int:
        if self.ispali(s):
            return 0 
        
        table = [None for i in range(len(s))]
        table[0] = 0
    
        #past_indices = [self.past_indices(s[:i+1]) for i in range(len(s))]
        for i in range(1,len(s)):
            index_list = self.past_indices(s[:i+1])
            #print(index_list)
            k_list = []
            for k in index_list:
                if k!= 0:
                    k_list.append(table[k-1] + 1)
                else: 
                    k_list.append(0)
            k_list.append(table[i-1] + 1)
            table[i] = min(k_list)
            #print(table[i])
        return table[-1]
            

    def past_indices(self, s:str) -> list[int]:
        ans = []
        for i in range(len(s)-1):
            if self.ispali(s[i::]) == True:
                ans.append(i)
        return ans 
    
    def ispali(self, s:str) -> bool: 
        #if s in self.brain:
        #    return self.brain[s]
        if s == s[::-1]:
        #    self.brain[s] = True 
            return True 
        #self.brain[s] = False 
        return False 

test = Solution()
print(test.minCut("ababbbabbaba"))