import heapq 

class Solution:
    def __init__(self):
        #below are the counts that will be useful to count the steps 
        self.repeats = [] #should be a heap 
        heapq.heapify(self.repeats) #this will contain repeats in the format (# of occurences in a row, character)
        self.total = 0 #total number of characters currently 
        self.lc_count = 0 #total number of lc characters 
        self.uc_count = 0 #total number of uc characters 
        self.digits_count = 0 #total number of digit characters 
        self.delcount = 0 
        self.addcount = 0 
        self.repcount = 0 

        #below are dictionaries containing the allowed characters by their segment 
        self.digits = {str(i) for i in range(10)}
        self.lc = {i for i in "abcdefghijklmnopqrstuvwxyz"}
        self.uc = {i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.other = {'.','!'}

    def strongPasswordChecker(self, password: str) -> int:
        self.parseString(password)
        valCheck = self.isValid(password)
        if valCheck == '0':
            return 0 #no changes needed! The string is already valid 

        elif valCheck == "1":
            self.case1(password)
            
        elif valCheck == "2":
            self.case2(password)
           
        elif valCheck == "3":
            self.case3(password) #after case 3 it is important to check whether we have come down and violated 1! 
            if self.isValid(password) == "1": #if we have violated case 1 in solving case three, lets solve for case 1! 
                self.case1(password)
        
        elif valCheck == "12":
            self.case12(password)
        
        elif valCheck == "13":
            self.case13(password)
        
        elif valCheck == "23":
            self.case23(password)

        elif valCheck == "123":
            self.case123(password)
        
        common = min(self.addcount,self.delcount) 
        final_ans = common + self.addcount - common + self.delcount - common + self.repcount 
        return final_ans
    
    def case123(self, password):
        print("entering123")
        if self.total < 6: #strategy here is to break 3s by inserting either lc_counter, uc_counter or digit_counter to break 3s 
            if self.lc_count < 1 and -1*self.repeats[0][0] >= 3 and self.total < 6: 
                self.heapAdd(self.repeats)
                self.lc_count += 1 
            
            if self.digits_count < 1 and -1*self.repeats[0][0] >= 3 and self.total < 6: 
                self.heapAdd(self.repeats)
                self.digits_count += 1 

            if self.uc_count < 1 and -1*self.repeats[0][0] >= 3 and self.total < 6: 
                self.heapAdd(self.repeats)
                self.uc_count += 1 
            
            valCheck = self.isValid(password)

            if self.isValid(password) == "12":
                return self.case12(password)
            
            elif valCheck == "23":
                return self.case23(password)
            
            elif valCheck == "13":
                return self.case13(password)
            
            elif valCheck == "1":
                return self.case1(password)
            
            elif valCheck == "2":
                return self.case2(password)
            
            elif valCheck == "3":
                return self.case3(password)


        elif self.total > 20: 
            self.specialCase(password)
    
    def case23(self,password):
        print("entering 23")
        if self.lc_count < 1:
            if -1*self.repeats[0][0] >= 3: 
                self.heapReplace(self.repeats)
                self.lc_count += 1 
            else: 
                self.repcount += 1 
                self.lc_count += 1 
        
        if self.uc_count < 1: 
            if -1*self.repeats[0][0] >= 3: 
                self.heapReplace(self.repeats)
                self.uc_count += 1 
            else: 
                self.repcount += 1 
                self.uc_count += 1 
        
        if self.digits_count < 1: 
            if -1*self.repeats[0][0] >= 3: 
                self.heapReplace(self.repeats)
                self.digits_count += 1 
            else: 
                self.repcount += 1 
                self.digits_count += 1 
        
        if -1*self.repeats[0][0] >= 3: 
            self.case3(password)
    
    def case13(self,password):
        print("entering13")
        if self.total > 20: 
            #write code to transfer heap contents to a tempheap [(mod3val, length, char)]
            tempheap = []
            heapq.heapify(tempheap)
            while self.repeats:
                curr = heapq.heappop(self.repeats)
                if -1*curr[0] >= 3: 
                    to_add = (-1*curr[0]%3, curr[0],curr[1])
                    heapq.heappush(tempheap,to_add)

            while tempheap and self.total > 20: 
                self.heapDelete(tempheap) 
            
            #write code to transfer heap contents back to original heap [(length, char)]
            while tempheap: 
                curr = heapq.heappop(tempheap)
                heapq.heappush(self.repeats,(curr[1],curr[2]))

            if self.total <= 20: 
                self.case3(password)
            else: 
                self.case1(password)

        elif self.total < 6: 
            while -1*self.repeats[0][0] >= 3 and self.total < 6: 
                self.heapAdd(self.repeats)
            
            if self.total >= 6: 
                self.case3(password)
            else: 
                self.case1(password)
    
    def specialCase(self, password):
        print("enteringSpecialCase")
        tempheap = []
        heapq.heapify(tempheap)
        while self.repeats:
            curr = heapq.heappop(self.repeats)
            if -1*curr[0] >= 3: 
                to_add = (-1*curr[0]%3, curr[0],curr[1])
                heapq.heappush(tempheap,to_add)

        while tempheap and self.total > 20: #after this step we lose either 1 or 3 or both 
            self.heapDelete(tempheap)

        while tempheap: 
            curr = heapq.heappop(tempheap)
            heapq.heappush(self.repeats,(curr[1],curr[2]))
        
        valCheck = self.isValid(password)

        if valCheck == "12":
            return self.case12(password)
        
        elif valCheck == "23":
            return self.case23(password)
        
        elif valCheck == "13":
            return self.case13(password)
        
        elif valCheck == "1":
            return self.case1(password)
        
        elif valCheck == "2":
            return self.case2(password)
        
        elif valCheck == "3":
            return self.case3(password)
        


    def case12(self, password):
        print("entering12")
        if self.total < 6: #first we add the number of chars that would satisfy 2. Check if 1 satisfied - if not then add the difference! 
            if self.lc_count < 1: 
                self.lc_count += 1 
                self.total += 1 
                self.addcount += 1 
            
            if self.uc_count < 1: 
                self.uc_count += 1 
                self.total += 1 
                self.addcount += 1 
            
            if self.digits_count < 1: 
                self.digits_count += 1 
                self.total += 1 
                self.addcount += 1 
            
            if self.total < 6: 
                self.case1(password)
        
        elif self.total > 20: 
            self.case1(password) #delete the difference to bring it down to 20 
            self.case2(password)
        
        
    
    def case1(self, password: str): #addition or deletion operation 
        print("entering 1")
        if self.total < 6: 
            self.addcount += 6-self.total 
            self.total = 6 
        elif self.total > 20: 
            self.delcount += self.total - 20 
            self.total = 20 
    
    def case2(self, password: str): #replacement operations 
        print("entering 2")
        if self.lc_count < 1: 
            self.repcount += 1 
            self.lc_count += 1 

        if self.uc_count < 1: 
            self.repcount += 1 
            self.uc_count += 1 

        if self.digits_count < 1: 
            self.repcount += 1 
            self.digits_count += 1 
        
    
    def case3(self, password:str): #satisfies 3 by replacing! - length unchanfed only repcount increases 
        print("entering 3")
        if self.repeats:
            while -1*self.repeats[0][0] >= 3: 
                curr = heapq.heappop(self.repeats)
                to_add1 = (curr[0]+3,curr[1]) #first part of breakage 
                to_add2 = (-2,curr[1]) 
                self.repcount += 1 
                heapq.heappush(self.repeats, to_add1)
                heapq.heappush(self.repeats,to_add2)
    
    def heapDelete(self, tempheap: heapq):#satisfies 3 by deleting 
        if tempheap: #if it is not already empty  
            curr = heapq.heappop(tempheap)
            to_add = (-1*(curr[1]+1)%3,curr[1]+1,curr[2])
            self.delcount += 1 
            if curr[2] in self.digits:
                self.digits_count -= 1
            elif curr[2] in self.uc:
                self.uc_count -= 1 
            elif curr[2] in self.lc:
                self.lc_count -= 1 
            self.total -= 1 
            if -1*to_add[1] >= 3: 
                heapq.heappush(tempheap, to_add)
    
    def heapAdd(self, heap: heapq):
        if -1*heap[0][0] >= 3: 
            curr = heapq.heappop(heap)
            to_add1 = (curr[0]+2, curr[1])
            to_add2 = (-2, curr[1])
            self.addcount += 1 
            self.total += 1 
            heapq.heappush(heap, to_add1)
            heapq.heappush(heap, to_add2)
    
    def heapReplace(self, heap: heapq):
        if -1*heap[0][0] >= 3: 
            curr = heapq.heappop(self.repeats)
            to_add1 = (curr[0]+3,curr[1]) #first part of breakage 
            to_add2 = (-2,curr[1]) 
            self.repcount += 1 
            heapq.heappush(self.repeats, to_add1)
            heapq.heappush(self.repeats,to_add2)
            

    
    def parseString(self, password: str) -> None: #this function parses the password and takes all the counts initially. It uses 2x passes to get all the info!
        #pass 1  
        for char in password:
            if char in self.lc:
                self.lc_count += 1 
            elif char in self.uc: 
                self.uc_count += 1 
            elif char in self.digits:
                self.digits_count += 1 
            self.total += 1 
        
        checked = set()
        #now lets get all the continuous frequencies in our heap! 
        i = 0
        tempstr = "" 
        while i<len(password):
            if tempstr:
                if password[i] == tempstr[-1]:
                    tempstr += password[i]
                
                else: 
                    if tempstr:
                        heapq.heappush(self.repeats,(-len(tempstr),tempstr[0]))
                    tempstr = password[i]
            else: 
                tempstr = password[i] 
            
            i+=1 

        if tempstr: 
            heapq.heappush(self.repeats,(-len(tempstr),tempstr[0]))
        
        return None 
    
    def isValid (self, password: str) -> str: #0 means it is valid, 1 means violated 1, 2 means violated 2, 3 means violated 3 
        print("entering isValid")
        ans = ""
        if self.total < 6 or self.total > 20: 
             ans += "1"
        if self.lc_count < 1 or self.digits_count < 1 or self.uc_count < 1: 
            ans += "2"
        
        if self.repeats:
            if -1*self.repeats[0][0] >= 3: 
                ans += "3"
        
        if not ans: 
            ans += "0"
        return ans
    
test  = Solution()
password = "1Abababcaaaabababababa"
print(test.strongPasswordChecker(password))