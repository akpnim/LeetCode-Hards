import math 
class Solution:
    def __init__(self):
        self.nums = {str(i) for i in range(10)}

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        nums = {str(i) for i in range(10)}
        abbr_list = []
        temp = ""
        for char in abbr: 
            if char not in nums:
                if temp != "":
                    abbr_list.append(temp)
                    temp = ""
                    
                abbr_list.append(char)
            else: 
                temp += char 
                if temp == "0":
                    return False 
        
        if temp != "":
            abbr_list.append(temp)
        
        counter_word = 0 
        counter_abbr = 0 

        while counter_word < len(word) and counter_abbr < len(abbr_list):
            if abbr_list[counter_abbr][0] in nums: 
                counter_word += int(abbr_list[counter_abbr])
                counter_abbr += 1 
            else: 
                if word[counter_word] == abbr_list[counter_abbr]:
                    counter_abbr += 1 
                    counter_word += 1 
                else: 
                    return False 
        
        if counter_word == len(word) and counter_abbr == len(abbr_list):
            return True 
        
        return False 
    
    def generateAbbreviations(self, word: str) -> list[str]:
        if len(word) == 1: 
            return ["1",word]

        else: 
            first_part = self.generateAbbreviations(word[0])
            second_part = self.generateAbbreviations(word[1::])
            ans = []
            for word1 in first_part:
                for word2 in second_part:
                    if word1[-1] in self.nums and word2[0] in self.nums: 
                        word1_limit = -1
                        word2_limit = len(word2)
                        for i in range(len(word1))[::-1]:
                            if word1[i] not in self.nums:
                                word1_limit = i 
                                break 
                        
                        for i in range(len(word2)):
                            if word2[i] not in self.nums:
                                word2_limit = i 
                                break 
                        
                        #print(word1,word2)
                        #print(word1_limit,word2_limit)
                        to_add = word1[:word1_limit+1] + str(int(word1[word1_limit::]) + int(word2[:word2_limit])) + word2[word2_limit::]
                        ans.append(to_add)
                    else:
                        ans.append(word1+word2)
        return ans 

    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        #Step 1 - lets get all the abbreviations of target
        temp_abbrevs = self.generateAbbreviations(target)
        target_abbrevs = []
        for abbrev in temp_abbrevs:
            target_abbrevs.append((self.getLength(abbrev),abbrev))
        target_abbrevs.sort()
        #print(target_abbrevs)
        #Step 2 - now lets compare each one 
        for abbrev in target_abbrevs:
            works = True  
            for word in dictionary:
                if self.validWordAbbreviation(word,abbrev[1]) == True: 
                    works = False 
                    break 
            if works == True: 
                return abbrev[1]
    
    def getLength(self, abbrev:str)  -> int: #returns the length of an abbrev string 
        count = 0 
        for i,char in enumerate(abbrev):
            if char not in self.nums:
                count += 1 
                if i>0 and abbrev[i-1] in self.nums:
                    count += 1 
        if abbrev[-1] in self.nums: 
            count += 1 
        return count 


test  = Solution()
target = "apple"
dictionary = ["blade"]
print(test.minAbbreviation(target,dictionary))
