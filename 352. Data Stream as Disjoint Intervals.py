class SummaryRanges:

    def __init__(self):
        self.prevlist = []
        self.running = []
        self.ans = []
        
    def addNum(self, value: int) -> None:
        self.running.append(value)
        
    def getIntervals(self) -> list[list[int]]:
        if self.prevlist == [] and self.running == []: 
            return [] 
        self.ans = [] #this is where we will store the intervals 
        self.all_sorted = [] #this is where we will store the final sorted array/ next prevlist 
        self.running.sort() #we sort the newly added running numbers 
        left = 0 
        right = 0 
        while left< len(self.prevlist) and right < len(self.running):
            if self.prevlist[left] <= self.running[right]:
                self.all_sorted.append(self.prevlist[left])
                left += 1 
            else: 
                self.all_sorted.append(self.running[right])
                right+= 1 
        
        while left< len(self.prevlist):
            self.all_sorted.append(self.prevlist[left])
            left+=1 
        
        while right< len(self.running):
            self.all_sorted.append(self.running[right])
            right += 1 

        self.prevlist = self.all_sorted
        self.running = []
        
        #now write code here to get the intervals now that sorting is sorted 
        i = 0 
        cur = []
        while i < len(self.prevlist):
            if i == 0: 
                cur = [self.prevlist[0]]

            else: 
                if self.prevlist[i] - self.prevlist[i-1] in [0,1]:
                    i+= 1 
                    continue
                else: 
                    cur.append(self.prevlist[i-1])
                    self.ans.append(cur)
                    cur = [self.prevlist[i]]
            i += 1 
        
        cur.append(self.prevlist[-1])
        self.ans.append(cur)
        return self.ans 
                
            