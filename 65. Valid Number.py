
# Invalid Test cases = "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "0" , "e" , "."
#Valid test cases = "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"
# case 1 - there is exponent 
# case 2 - no exponent 


class Solution:
    def __init__(self):
        self.digits = {"0","1","2","3","4","5","6","7","8","9"}
        self.deci = {"0","1","2","3","4","5","6","7","8","9","."}
    def isNumber(self, s: str) -> bool:
        #case 1 where there is an exponent 
        if 'e' in s or 'E' in s: 
            index_e = max(s.find('e'),s.find('E'))
            if self.isExponent(s[index_e::]):
                if self.isDecimal(s[:index_e]) or self.isInteger(s[:index_e]):
                    return True 
                else:
                    return False 
            else:
                return False 
        if self.isDecimal(s) or self.isInteger(s):
            return True 
        return False 
    
    def isInteger(self, s:str) -> bool: 
        if s == "":
            return False 
        countDigit = 0
        for char in s:
            if char in self.digits: 
                countDigit+= 1 
        if len(s) - countDigit > 1: 
            return False 
        if len(s) - countDigit == 1: 
            if s[0] == '+' or s[0] == "-":
                return self.isInteger(s[1::]) #possible improvement here
            else: 
                return False 
        return True 
    
    def isDecimal(self, s:str) -> bool: 
        not_allowed = 0 
        for char in s: 
            if char not in self.deci:
                not_allowed += 1
        if not_allowed > 1:
            return False 
        if not_allowed == 1: 
            if s[0] == '+' or s[0] == '-':
                return self.isDecimal(s[1::])
            else:
                return False 
        if s.count('.') != 1:
            return False 
        if self.isDigit(s[:-1]) == True and s[-1] == '.':
            return True
        if s[0] == '.' and self.isDigit(s[1::]) == True:
            return True 
        if self.isDigit(s[:s.find('.')]) == True and self.isDigit(s[s.find('.')+1::]) == True:
            return True
        else:
            return False 
        
    
    def isDigit(self, s:str) -> bool:
        if s =="":
            return False 
        for char in s:
            if char not in self.digits:
                return False 
        return True 
    
    def isExponent(self, s:str) -> bool: 
        if s[0] == 'e' or s[0] == 'E':
            if self.isInteger(s[1::]):
                return True 
        return False 

test = Solution()

print(test.isInteger("1323"))
print(test.isDecimal("."))
print(test.isExponent("E213"))
print(test.isNumber("-1.1123123"))