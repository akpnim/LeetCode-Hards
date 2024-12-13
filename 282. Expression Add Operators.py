class Solution:
    def __init__(self):
        self.combos = []
        self.ops = ["","*","+","-"]
        self.digs = {'0','1','2','3','4','5','6','7','8','9'}

    def addOperators(self, num: str, target: int) -> list[str]:
        ans = []
        all_combos = self.createCombos(num)
        #print(all_combos)
        for combo in all_combos:
            if eval(combo) == target: 
                ans.append(combo)
        return ans 
    
    def getOps(self, n:int, k:int, inp: list[int]):
        if n == k: 
            self.combos.append(inp)
            return 
        for op in self.ops: 
            self.getOps(n,k+1,inp+[op])
        

    def createCombos(self,num:str) -> list[str]:
        self.getOps(len(num)-1,0,[])
        ans = [] 
        for combo in self.combos: 
            to_add = ""
            for i,op in enumerate(combo):
                to_add = to_add + num[i] + op
            to_add += num[-1]
            #print(to_add)
            if self.isLeading(to_add) == False:
                ans.append(to_add)
        #print(ans)
        return ans 
    
    def isLeading(self, exp: str) -> str: 
        switch = True
        for i,char in enumerate(exp):
            if switch == True and char == '0':
                if i<len(exp) - 1: 
                    if exp[i+1] in self.digs:
                        return True 
            elif char in self.digs:
                switch = False 
                continue 
            elif char not in self.digs:
                switch = True 

        return False 

    
test = Solution()
num = "105"
target = 5
print(test.addOperators(num,target))