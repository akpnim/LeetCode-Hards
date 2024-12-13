#step 1: create a dictionary with key as the list items and the values as the indices for easy lookup 
#step 2: create a list with the index as the index and the values as a list of k-values 
#step 3: keep the original list as the list on which binSearch will work with left and right indices specified 

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        #step 1 
        mydict = {}
        for i,val in enumerate(stones):
            mydict[val] = i 
        #step 2 
        mylist = [set()for i in range(len(stones))]
        mylist[0].add(0) #initializing k 
        #step3 
        for i, val in enumerate(stones):
            for k in mylist[i]:
                checkVals = [val+k-1, val+k, val+k+1]
                for checkval in checkVals:
                    if checkval > val: #preserving the strictly increasing order 
                        if checkval in mydict:
                            ind = mydict[checkval]
                            to_add = checkval - val 
                            if checkval not in mylist[ind]:
                                mylist[ind].add(to_add)
        
        #print(mylist)
        if mylist[-1]:
            return True 
        return False 

test = Solution()
stones = [0,1,3,5,6,8,12,17]
test.canCross(stones)


