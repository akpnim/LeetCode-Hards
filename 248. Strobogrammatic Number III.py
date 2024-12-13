class Solution:
    def __init__(self):
        self.brain = {}
        self.brain[1] = ['0','1','8']
        self.brain[2] = ['11','69','88','96']
        self.zeroes = {}
        self.zeroes[1] = ['0']
        self.zeroes[2] = ['00']
    
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mainlist = []
        for n in range(len(low),len(high)+1): 
            mainlist+=self.findStrobogrammatic(n)
        maindict = {i for i in mainlist}
        counter = 0 
        for num in maindict:
            if int(num) >= int(low) and int(num)<= int(high):
                counter += 1 
        return counter 
 
    def findStrobogrammatic(self, n: int) -> list[str]:
        if n in self.brain: 
            return self.brain[n]
        
        ans = set()
        prev = self.findStrobogrammatic(n-2) #prev is this plus zero strobo for n-2!!! 
        if n>3:
            prev = prev + self.findZstr(n-2)
        for ends in self.brain[2]:
            for mid in prev:
                to_add = ends[0] + mid + ends[1]
                if to_add not in ans: 
                    ans.add(to_add)
        self.brain[n] = [i for i in ans]
        return self.brain[n]
    
    def findZstr(self, n: int) -> list[str]:
        if n in self.zeroes:
            return self.zeroes[n]
        
        ans = []
        prev = self.findStrobogrammatic(n-2) + self.findZstr(n-2)
        for ends in self.zeroes[2]:
            for mid in prev:
                to_add = ends[0] + mid + ends[1]
                ans.append(to_add)
        self.zeroes[n] = ans 
        return ans 