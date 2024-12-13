#can improve by counting the number of left brackets to be removed and also the number of right brackets to be removed and doing a more efficient backtracking 
class Solution:
    def __init__(self):
        self.brackets = None 
        self.poss = []
        self.ansdict = set()

    def removeInvalidParentheses(self, s: str) -> list[str]:
        openstack = []
        closedstack = []
        brackets = []
        for i,char in enumerate(s):
            if char == '(':
                openstack.append(char)
                brackets.append(i)
            elif char == ')':
                brackets.append(i)
                if openstack:
                    openstack.pop()
                else: 
                    closedstack.append(char)
        self.brackets = brackets
        count = len(openstack) + len(closedstack) #this is how many brackets need to be deleted!
        self.dfs(set(),[],count) #basically a way to backtrack and get all combinations 
        ansdict = set()
        for combo in self.poss: 
            tempans = ""
            prevind = 0
            for i,index in enumerate(combo):
                tempans += s[prevind:index]
                prevind = index + 1 
            tempans += s[prevind::]
            if self.isValid(tempans):
                ansdict.add(tempans)
        return [i for i in ansdict]

        

    
    def dfs(self, mydict: set, mylist: list[int], count:int):
        if len(mylist) == count: 
            self.poss.append(mylist)
            return 
        for num in self.brackets: 
            if num not in mydict:
                if not mylist:
                    self.dfs(mydict.union({num}) , mylist + [num],count)
                elif num > mylist[-1]:
                    self.dfs(mydict.union({num}) , mylist + [num],count)



    def isValid(self, s:str) -> bool: 
        openstack = []
        closedstack = []
        for i,char in enumerate(s):
            if char == '(':
                openstack.append(char)
            elif char == ')':
                if openstack:
                    openstack.pop()
                else: 
                    closedstack.append(char)
        count = len(openstack) + len(closedstack) #this is how many brackets need to be deleted!
        if count == 0: 
            return True
        else: 
            return False 

test = Solution()
print(test.removeInvalidParentheses("()())()"))