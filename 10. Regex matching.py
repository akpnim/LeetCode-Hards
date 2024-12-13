#changed all the .* characters to *
#Added functionality to handle .* 
#356/356 passed 

class Solution: 
    def logical_mess(self,s:str, p:str) -> bool: 
        alphabet = "abcdefghijklmnopqrstuvwxyz."
        print(s,p,"sp")

        if s=="" and p=="":
            print("here1")
            return True 
        
        if s=="" and p == None:
            "print here2"
            return True 
        
        if s == "" and len(p) == 1: 
            "print here3"
            return False 
        
        if s == "" and p == ".*":
            return True 
        
        if s == "" and len(p) == 2 and "*" in p: 
            return True
        
        if '*' not in p and '.' not in p: 
            if s==p:
                return True 
            else: 
                print("line32")
                return False 
        #base case for logical mess is below 
        if "*" not in p: 
            if len(p) != len(s):
                print("line 37",p,s)
                return False 
            for i,char in enumerate(p): 
                if char != '.' and char != s[i]:
                    print("line41")
                    return False 
            print("here4")
            return True 
        
        #lets do a three way split from 'alphabet'
        if '.' in p: 
            if p == '.':
                if len(s) == 1: 
                    return True 
            if p == '.*'*(int(len(p)/2)):
                return True 
            
            if ".*" in p:
                return True 
            
            if p==s:
                return True 
            
            for i,char in enumerate(p):
                if i == len(p) -1: 
                    if char == '.':
                        return self.logical_mess(s[:len(s)-1],p[:len(p)-1]) and self.logical_mess(s[len(s)-1],p[len(p)-1])
                elif i!= len(p) -1:
                    if char == '.' and p[i+1] != '*':
                        s_splits =  self.all_three_splits(s)
                        for split in s_splits:
                            candidate = self.logical_mess(split[0],p[:i]) and self.logical_mess(split[1],p[i]) and self.logical_mess(split[2],p[i+1::])  
                            if candidate == True: 
                                print("here5")
                                return True 
                        print("hereeewqfqewfe")
                        return False 
                    if ".*" in p and p.count('.') == 1:
                        return True 

        
        if '*' in p and '.' not in p: 
            print("HERER", s,p)
            if s=="":
                return True 
            if len(p) == 2:
                if s == p[0]:
                    return True 
            edited_p = p 
            s_group = self.group_s(s)
            print("group = ",s_group)
            for char in s_group: 
                ind = edited_p.find(char[0])
                if ind == -1: 
                    print('hereeeeeeee')
                    print(edited_p,char[0])
                    return False 
                edited_p = edited_p[ind+2::]
            return self.logical_mess("",edited_p)


    def all_three_splits(self, s:str) -> list:
        ans = []
        for i,char in enumerate(s):
            ans.append([s[:i],s[i],s[i+1::]])
        return ans 
    
    def group_s(self,s):
        total = ""
        ans = [] 
        if len(s) == 1: 
            return s 
        for i,char in enumerate(s):
            if total == "":
                total += char 
                continue 
            if char==total[-1]:
                total += char
            elif char != total[-1]:
                ans.append(total)
                total = char 
            if i == len(s) -1:
                ans.append(total)
        return ans 
    
    def isMatch(self, s:str,p:str) -> bool:
        #the first section deals with finding the pillars/pivots aka the alphabets that are certain 
        print("s,p = ", s,p)
        if s == "" and p=="":
            return True 
        
        #case 1 - input p does not contain any special characters 
        if "*" not in p and '.' not in p:
            if len(s) != len(p):
                print("line125",s,p)
                return False 
            if p == s: 
                return True 
            elif p!= s: 
                return False 
        
        #case 2 - only dot plus alphabet - if length mismatch then false ofc and if char doenst match then false  
        if "." in p and "*" not in p:  
            if len(p) != len(s):
                return False 
            else: 
                for i,char in enumerate(p):
                    if char != ".":
                        if char != s[i]:
                            print("line140")
                            return False 
            "15000LINE"
            return True 
#Below is the case for when .* is in p; - the interesting case to note is if .* is BEFORE the pivot... then s.find 
        pillar = ""
        pivot_position = None 
        for i,char in enumerate(p):
            if i == len(p) - 1 and char not in "*":
                pillar += char
                pivot_position = i-len(pillar)+1
                break 
            if char in "*" and pillar!="":
                pivot_position =i-len(pillar)-1
                break 
            if i==len(p) - 1 and char not in "*":
                pillar += char
            if i!= len(p) -1 and char not in "*" and p[i+1] not in "*":
                pillar += char
        
        #if ".*" in p and pivot_position == None:
        if p==".*":
            return True 
            pillar = ".*"
            #pivot_position = None 
        
        print("piller", p,pillar, pivot_position,s)
        #pivot is None if there is no pillar (including no dot pillars)
        if pivot_position == None: 
            print("entering logical mess: ",s,p)
            return self.logical_mess(s,p)
    #The below first section deals with the case of splitting s up into pillar's lengths so can match fairly 
        list_s = []
        for i,j in enumerate(s):
            to_add = s[i:i+len(pillar)]
            if len(to_add) == len(pillar):
                list_s.append(to_add)

        print(list_s)

        s_positions = [] 
        for i,chars in enumerate(list_s):
            ans =  True 
            for j,char in enumerate(chars): 
                if char != pillar[j] and pillar[j] != '.':
                    ans = False 
            if ans == True: 
                s_positions.append(i)
        print(s_positions)

        if s==p:
            print('here')
            return True 
    #the longer case is when pivot doesnt exist i,e, only elements with .*a* exist
        for s_position in s_positions:
            if s_position == -1: 
                print('line 139',pillar)
                return False 
            print("Exiting",s_position,s,pivot_position,pillar,p)
            candidate = self.isMatch(s[:s_position],p[:pivot_position]) and self.isMatch(s[s_position:s_position+len(pillar)],p[pivot_position:pivot_position+len(pillar)]) and self.isMatch(s[s_position+len(pillar)::],p[pivot_position+len(pillar)::])
            if candidate == True: 
                return True 
        print("ENTERED200line",s,p,list_s)
        
        list_p = p.partition(".*")
        ind_left = s.find(list_p[0])
        ind_right = s.rfind(list_p[2])

        if list_p[0] == "" and list_p[2] == "":
            return True 
        
        if list_p[0] == "" and ind_right == len(s)-1 and len(s)>1:
            return True 
        
        elif list_p[0] == "" and ind_right != len(s)-1:
            return False 
        
        if list_p[2] == "" and ind_left == 0:
            return True 
        
        elif list_p[2] == "" and ind_left != 0: 
            return False 

        if ind_left == -1 or ind_right == -1:
            return False 
        if ind_left <= ind_right:
            print("itthee 206")
            return True 
        return False 

def main():
    a = Solution()
    s = "abcaaaaaaabaabcabac" #the original input string s 
    p = ".*ab.a.*a*a*.*b*b*" #the regular expression
    print(a.isMatch(s,p))

main()