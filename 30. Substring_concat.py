
class Solution:

    def findSubstring(self, s: str, words: list[str]) -> list[int]:  
        if len(words) == len(s):
            return [0]      
        wordLen = len(words[0])
        answer = []
        for i in range(len(s)-wordLen*len(words)+1):
            window = s[i:i+wordLen*len(words)]
            to_add = self.search(window,words,wordLen)
            if to_add == True:
                answer.append(i)
        return answer 
    
    def partString(self,s: str, length: int) -> list[str]:
        ans2 = []
        i = 0 
        while i<=len(s):
            if s[i:i+length]:
                ans2.append(s[i:i+length])
            i = i + length 
        return ans2 
    
    def search(self, s:str, words: list[str], length: int) -> bool:
        p = self.partString(s,length)
        if sorted(words) == sorted(p):
            return True 
        else: 
            return False 