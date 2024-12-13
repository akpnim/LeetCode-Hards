#6,0 and 8,9; baabbaa and b 
class Solution:     
    def __init__ (self):
        self.brain = {}
        self.suff = {}

    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        ans = [] 
        for i,word in enumerate(words):
            self.brain[word] = i 
        
        for i,word in enumerate(words):
            for j,letter in enumerate(word):
                if word[j::] in self.suff:
                    self.suff[word[j::]].append(i)
                else: 
                    self.suff[word[j::]] = [i]
        
        for i,word in enumerate(words):
            if word == "":
                for j,word2 in enumerate(words):
                    if i!=j:
                        if self.isPali(word,word2):
                            ans.append([i,j])
                            ans.append([j,i])
            else: 
                suffixs = self.findSuffix(word)
                #print(suffixs,word)
                for suffix in suffixs:
                    if suffix in self.suff: 
                        for index in self.suff[suffix]:
                            if index != i: 
                                if self.isPali(word, words[index]) == True: 
                                    ans.append([i,index])
        return ans        

    def isPali(self, str1: str, str2: str ) -> bool: 
        sumstr = str1 + str2 
        if sumstr == sumstr[::-1]:
            return True 
        return False 

    def findSuffix(self, word: str) -> list[str]: #fix the find suffix fuction!
        ans = []
        temp = set()
        for letter in word: #special case of perfect palindrome 
            temp.add(letter)
        if len(temp) == 1: 
            a = [i for i in temp]
            ans.append(a[0])
            ans.append("")
            #print(ans)
            return ans
        
        word = word[::-1]
        i = self.longestPali(word[:-1])
        ans.append(word[i+1::])

        if word == word[::-1]:
            ans.append("")
        
        return ans 
    
    def longestPali(self, word: str) -> int:
        for i in range(len(word))[::-1]:
            left = 0 
            right = i 
            while word[left] == word[right]:
                right -= 1 
                left += 1 
                if left >= right: 
                    return i 
    
            

test = Solution()
words = ["a","aa","aaa"]
print(test.palindromePairs(words))