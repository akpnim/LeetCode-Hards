from collections import deque

class Solution:

    def __init__(self):
        self.dictionary = {}

    def minWindow(self, s: str, t: str) -> str:
        self.createDict(t)
        ranges = []
        local_dict = {i:self.dictionary[i] for i in self.dictionary}
        checker = {i:deque([]) for i in self.dictionary}
        queue = deque([])
        for i,char in enumerate(s):
            if char in local_dict:
                if local_dict[char] > 0: 
                    checker[char].append(i)
                    local_dict[char] -= 1 
                elif local_dict[char] == 0: 
                    checker[char].popleft()
                    checker[char].append(i)
                if {i:len(checker[i]) for i in checker} == self.dictionary:
                    min_list = [checker[char][0] for char in checker]
                    max_list = [checker[char][-1] for char in checker]
                    if not ranges: 
                        ranges = [min(min_list),max(max_list)]
                    else: 
                        if ranges[1] - ranges[0] > max(max_list) - min(min_list):
                            ranges = [min(min_list),max(max_list)]

        if ranges == []:
            return ""
        return s[ranges[0]:ranges[1]+1]
    
    def createDict(self,t:str) -> None: 
        for char in t: 
            if char in self.dictionary:
                self.dictionary[char] += 1 
            else: 
                self.dictionary[char] = 1 


test = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(test.minWindow(s,t))