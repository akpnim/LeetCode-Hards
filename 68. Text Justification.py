class Solution:

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        if words == []:
            return []
        
        if self.isLastLine(words,maxWidth):
            ans = ' '.join(words)
            ans = ans + ' '*(maxWidth - len(ans))
            return [ans]
        
        max_index = self.findLimit(words,maxWidth) 
        curr_line = self.getLine(words[:max_index+1],maxWidth)
        print("words = ", words)
        print("max_index = ",max_index)
        print("curr_line = ",curr_line)

        return [curr_line] + self.fullJustify(words[max_index+1::],maxWidth)
        

    def isLastLine(self, words: list[str], maxWidth: int) -> bool: 
        if self.countLetters(words) + len(words) - 1 <= maxWidth:
            return True 
        else: 
            return False 

    def countLetters(self, words: list[str]) -> int: 
        count = 0 
        for word in words: 
            count += len(word)
        return count 
    
    def findLimit(self,words: list[str],maxWidth: int) -> int:
        if len(words) == 1: 
            return 0 
        word_count = -1
        ans = 0 
        for i,word in enumerate(words): 
            word_count += len(word) + 1 
            if word_count <=maxWidth:
                ans = i 
        return ans  
    
    def getLine(self, words: list[str], maxWidth: int) -> str: 
        if len(words) == 1: 
            return words[0] + ' '*(maxWidth-len(words[0]))
        line = words[0]
        spacing = self.getSpacing(words,maxWidth)
        for i,space in enumerate(spacing): 
            line += space*' '
            line += words[i+1]
        return line

    
    def getSpacing(self,words: list[str], maxWidth: int) -> list[int]: #can be improved the way split is done 
        if len(words) == 1: 
            return [maxWidth-len(words[0])]
        total_used = self.countLetters(words) + len(words) -1 
        diff = maxWidth - total_used
        diff_list = [1+ diff//(len(words)-1) for i in range(len(words)-1)]
        remainder = diff - (diff//(len(words)-1)) * (len(words) -1) 
        for i,spacing in enumerate(diff_list):
            if remainder!= 0: 
                diff_list[i] += 1 
                remainder -= 1 
            if remainder == 0: 
                break 
        return diff_list


    
test = Solution()

#print(test.isLastLine([ "text", "justifican."],16))

#print(test.fullJustify([ "text", "justifican."],16))

print("limits",test.findLimit(['enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'],20))

#print(test.getSpacing([ "text", "justifican.", "12", "1"],20))

#print(test.getLine([ "text", "justifican.", "12"],20))

print(test.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to",
                        "a","computer.","Art","is","everything","else","we","do"],20))
