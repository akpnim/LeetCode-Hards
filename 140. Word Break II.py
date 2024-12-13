class Solution:
    def __init__(self):
        self.brain = {}
        self.storage = []

    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        self.brain = wordDict
        if s in self.brain:
            return [s]
        self.computeString(s,"")
        return self.storage
    
    def computeString(self, s:str, prev: str) -> None: 
        if s in self.brain: 
            if prev[0] == " ":
                self.storage.append(prev[1::] + " " + s)
            else: 
                self.storage.append(prev + " " + s)
        
        for i in range(1, len(s)):
            if s[:i] in self.brain: 
                self.computeString(s[i::], prev + " " + s[:i])
        return 
    
test = Solution()
s = "aaaaaaa"
wordDict = {"aaaa","aa","a"}
print(test.wordBreak(s,wordDict))