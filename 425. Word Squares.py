class Solution:
    def __init__(self):
        self.prefix_table = {}
        self.ans = []
        self.words = []

    def wordSquares(self, words: list[str]) -> list[list[str]]:
        self.words = words 
        #building the prefix table roughly to test things out 
        for word in words: 
            for i in range(1,len(word)+1):
                if word[:i] in self.prefix_table:
                    self.prefix_table[word[:i]].append(word)
                else: 
                    self.prefix_table[word[:i]] = [word]
        
        n = len(words[0])
        self.recursive([],n)
        return self.ans 
        
    def recursive(self, temp: list[str], n: int):
        if n == 0: 
            self.ans.append(temp)
            return 
        
        if temp == []:
            for word in self.words: 
                self.recursive(temp+[word],n-1)
        else: 
            findstr = ""
            i = len(temp)
            for word in temp: 
                findstr += word[i]
            
            if findstr in self.prefix_table:
                for word in self.prefix_table[findstr]:
                    self.recursive(temp + [word], n-1)
    

test = Solution()
words = ["ball","baller","mall"]
print(test.wordSquares(words))
