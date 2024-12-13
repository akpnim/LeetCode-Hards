class Solution:
    def __init__(self):
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.alphabets = {i for i in self.alphabets}
        self.remember = {}

    def isMatch(self, s: str, p: str) -> bool:
        if s == "":
            if p=="":
                return True 
            if len(p) - p.count('*') > 0: 
                return False 
            else: 
                return True 
            
        pivot = ""
        for i,char in enumerate(p): 
            if i< len(p) - 1: 
                if char in self.alphabets and p[i+1] not in self.alphabets:
                    pivot += char
                    break 
                elif char in self.alphabets and p[i+1] in self.alphabets:
                    pivot+= char 
                    continue 
            elif i== len(p) - 1: 
                if char in self.alphabets:
                    pivot += char 
                    break 
        #remember to consider the case where pivot == "" but p!= "" i.e. alphabets not in p 
        s_pivot_index = s.find(pivot)
        if s_pivot_index == -1: 
            return False 


        if pivot == '':#this is the case where there are no alphabets but only * and ?  
            if p== "" and s=="":
                return True 
            elif p=="" and s!="":
                return False 
            if '?' not in p and '*' in p: 
                return True 
            if '?' in p and '*' not in p: 
                if p.count('?') != len(s):
                    return False  
                else: 
                    return True 
            if '?' in p and '*' in p:
                if p.count('?') <= len(s):
                    return True 
                else:
                    return False 
        
        all_splits = self.posplits(s,pivot)
        p_split = p.split(pivot,1)

        for s_split in all_splits:
            left = None 
            if (s_split[0],p_split[0]) in self.remember:
                left = self.remember[(s_split[0],p_split[0])]
            if left == None: 
                left = self.isMatch(s_split[0],p_split[0])
                self.remember[(s_split[0],p_split[0])] = left 
            
            right = None 
            if (s_split[1],p_split[1]) in self.remember:
                right = self.remember[(s_split[1],p_split[1])]
            if right == None: 
                right = self.isMatch(s_split[1],p_split[1])
                self.remember[(s_split[1],p_split[1])] = right  
            
            check =  left and right 

            if check == True: 
                return True 

        return False 

    def posplits(self,s,pivot):
        fragments = []
        for i in range(len(s)):
            fragments.append(s[i:i+len(pivot)])
        splits = []
        for i,fragment in enumerate(fragments):
            if fragment==pivot: 
                left = s[:i]
                right = s[i+len(pivot)::]
                splits.append([left,right])
        return splits 


test = Solution()

test_s = "adasdasdabcsasdsadabcsasdasdabc"
test_p = "?*?*abcs**??*?abc"
test_s = "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
test_p = "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"


print(test.isMatch(test_s,test_p))
