class Solution:
    def __init__(self):
        self.digs = {str(i) for i in range(10)}
        self.stack = [] #keeps track of bracket depth
        self.sign = []
        self.closed = []
        
    def calculate(self, s: str) -> int:
      
        parity = True
        curtotal = 0 
        numstring = ""

        if s == "": #base case 
            return curtotal 

        for i,char in enumerate(s):
            if char == '-':
                parity = False 
                continue 
            
            if char == '+':
                parity = True 
                continue

            if char == '(': 
                self.stack.append(curtotal)
                self.sign.append(parity)
                curtotal = 0 
                parity = True 
            
            if char == ')':
                check = self.sign.pop()
                if check == True: 
                    curtotal = self.stack.pop() + curtotal
                else: 
                    curtotal = self.stack.pop() - curtotal
                if self.stack == []:
                    self.closed.append(curtotal) 
            
            if char in self.digs: #account for prevparity 
                numstring += char 
                if i == len(s) -1 or s[i+1] not in self.digs:
                    if parity == True: 
                        curtotal += int(numstring)

                    elif parity == False: 
                        curtotal -= int(numstring)
                    numstring = ""

        return curtotal 

test = Solution()

s ='1+ 1 -1 -(1-2)'#Facug a challeing with this test case if we make it negative then the answer is wrong
print(test.calculate(s))
        
        
        
        
