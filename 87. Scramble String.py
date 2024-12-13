class Solution:
    def __init__(self):
        self.brain = {}
        
    def isScramble(self, s1: str, s2: str) -> bool: 

        if s1 == s2:
            return True 
        
        if len(s1) != len(s2):
            return False 
        
        sets1 = {char for char in s1}
        sets2 = {char for char in s2}
        if sets1 != sets2: 
            return False 
        if sets1 == sets2 and len(s1) <= 3: 
            return True 
        
        for char in s1:
            if s2.count(char) != s1.count(char):
                return False 
        
        first = s1[0]
        for i in range(len(s2)-1):
            left_s2 = s2[:i+1]
            right_s2 = s2[i+1::]
            #print(left_s2,right_s2)
            #print(s1[:len(left_s2)],s1[len(left_s2)::])
            if first in left_s2:
                if (s1[:len(left_s2)],left_s2) not in self.brain:
                    self.brain[(s1[:len(left_s2)],left_s2)] = self.isScramble(s1[:len(left_s2)],left_s2)
                
                if (s1[len(left_s2)::],right_s2) not in self.brain: 
                    self.brain[(s1[len(left_s2)::],right_s2)] = self.isScramble(s1[len(left_s2)::],right_s2)

                if self.brain[(s1[:len(left_s2)],left_s2)] == True and self.brain[(s1[len(left_s2)::],right_s2)] == True:
                    return True 
        
            if first in right_s2:
                if (s1[:len(right_s2)],right_s2) not in self.brain: 
                    self.brain[(s1[:len(right_s2)],right_s2)] = self.isScramble(s1[:len(right_s2)],right_s2)
                
                if (s1[len(right_s2)::],left_s2) not in self.brain: 
                    self.brain[(s1[len(right_s2)::],left_s2)] = self.isScramble(s1[len(right_s2)::],left_s2) 

                if  self.brain[(s1[:len(right_s2)],right_s2)] == True and  self.brain[(s1[len(right_s2)::],left_s2)] == True:
                    return True     
                
        return False 


s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
test = Solution()
ans = test.isScramble(s1,s2)
print(ans)
