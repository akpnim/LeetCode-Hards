class Solution:
    def __init__(self):
        self.brain = {}

    def countDigitOne(self, n: int) -> int:
        strN = str(n)
        sum = 0 
        for index,digit in enumerate(strN[::-1]):
            if int(digit) > 1:
                sum += 10**index + int(digit)*self.base(index-1)
            elif int(digit) == 1: 
                right_add = strN[::-1][:index][::-1]
                if not right_add:
                    right_add = '0' 
                sum += self.base(index-1) + int(right_add) + 1 
        return sum 
    

    def base(self, index: int) -> int: 
        #base case/memoization check  
        if index in self.brain:
            return self.brain[index]
        
        if index == -1: 
            self.brain[index] = 0 
            return self.brain[index]
        
        if index == 0: 
            self.brain[index] = 1 
            return self.brain[index]
        
        else: 
            ans = 10**index + 10* self.base(index-1)
            self.brain[index] = ans 
            return self.brain[index]

test = Solution()
print(test.countDigitOne(11))