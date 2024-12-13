from collections import deque 

class Solution:
    def __init__(self):
        self.mydict = set()

    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        #intiial part of the code converts nums into segments that we care about in O(n) time. 
        k = indexDiff
        segments = []
        temp = []
        for num in nums:
            temp.append(num)
            if len(temp) == k+1: 
                segments.append(temp)
                temp = [] 
        if temp!= []:
            segments.append(temp)
        
        #The next part will deal with the main part of the code 
        for i,seglist in enumerate(segments):
            queue1 = deque([i for i in seglist])
            if i < len(segments) - 1: 
                queue2 = deque([i for i in segments[i+1]])
            else: 
                queue2 = deque([])
            sortedlist = sorted(seglist)

            
            for i in range(1,len(sortedlist)):
                if abs(sortedlist[i] - sortedlist[i-1]) <= valueDiff:
                    return True 
            
            while queue2:
                self.mydict.add(queue1.popleft())
                checkVal = queue2.popleft()
                print(checkVal)
                ind = self.binSearch(sortedlist, checkVal)

                if ind> -1:
                    if sortedlist[ind] not in self.mydict:
                        if abs(checkVal-sortedlist[ind]) <= valueDiff:
                            return True
                    
                if ind<len(sortedlist) -1: 
                    if sortedlist[ind+1] not in self.mydict:
                        if abs(checkVal-sortedlist[ind+1]) <= valueDiff:
                            return True 
        return False 

    def binSearch(self, sortedlist: list[int], checkVal: int) -> int: #returns the value of the index after which checkVal should go
        base = 0
        ceiling = len(sortedlist) - 1 

        while True: 
            curr = base + ((ceiling - base)//2)
        
            if checkVal >= sortedlist[curr+1] and curr+1 == len(sortedlist) - 1:
                return curr + 1 
                
            if checkVal <= sortedlist[curr] and curr == 0:
                return curr - 1 
            
            if checkVal >= sortedlist[curr] and curr != len(sortedlist) - 1:
                if checkVal <= sortedlist[curr+1]:
                    return curr 
            
            if checkVal < sortedlist[curr]:
                ceiling = curr 
                
            if checkVal >= sortedlist[curr]: 
                base = curr 


test = Solution()
nums = [1,2,5,6,7,2,4]
print(test.containsNearbyAlmostDuplicate(nums,4,0))