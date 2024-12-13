#idea - deleting the prefix if current == prefix and current in words. small speedup mayble. 

class Solution: 
    def __init__(self):
        self.prefixes = set()
        self.table = None 
        self.words = None 
        self.ans = set() #set of answers 
        self.m = 0
        self.n = 0 

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        for word in words: #initializing prefix set (max 300,000 entries)
            for i in range(1,len(word)+1):
                self.prefixes.add(word[:i])
        #initializing key variables 
        self.table = board 
        self.words = {i for i in words}  #easy lookup words dict 
        self.m = len(self.table)
        self.n = len(self.table[0])
        for i, row in enumerate(self.table):
            for j,column in enumerate(self.table[0]):
                self.backtrack((i,j),"",set())
                if len(self.words) == 0: #remember to delete from self.words once a word is found and also to delete from self.prefixes 
                    break 
            if len(self.words) == 0: 
                break 
        return [i for i in self.ans] 
        
    def backtrack(self, start:tuple[int], form:str, visited: set[tuple[int]]):
        form = form + self.table[start[0]][start[1]] #adding to current formed word 
        #print(form)
        visited.add(start)
        if form not in self.prefixes:
            #print(form," not in preixes") #if the current form is not in prefixes then go back! 
            return 
        
        if form in self.words: 
            self.ans.add(form)
            #print("ANS = ", self.ans)
            #self.prefixes.remove(form)
            #self.words.remove(form)

        neighs = self.getNeigh(start)
        #print(form,neighs,visited)
        for neigh in neighs: 
            if neigh not in visited: 
                self.backtrack(neigh,form,visited)
                visited.remove(neigh)


    def getNeigh(self, coor:tuple[int]) -> list[tuple[int]]: #gives all the neighbors' coordinates
        ans = []
        if coor[0] >= 1: 
            ans.append((coor[0]-1, coor[1]))
        if coor[0] < self.m - 1: 
            ans.append((coor[0] + 1, coor[1]))
        if coor[1] >= 1:
            ans.append((coor[0],coor[1] - 1))
        if coor[1] < self.n - 1: 
            ans.append((coor[0],coor[1] + 1))
        return ans

test = Solution()
table = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
print(test.findWords(table,words))