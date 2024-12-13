from sortedcontainers import SortedList 
import math 
#Three step approach:
#step 1: double for loop for each column pair 
#step 2: update rowsums and then cumsums for each column pair 
#step 3: use SortedList to find closest match 
class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:  
        answers = []
        for i in range(len(matrix[0])):#column 1 
            rowSums = [0 for i in range(len(matrix))]#initializing rowsums 
            for j in range(i,len(matrix[0])):#column 2 
                for p in range(len(matrix)):
                    rowSums[p] += matrix[p][j] 
                cumSum = []
                sumCum = 0 
                for element in rowSums:#creating cumSum for each column pair 
                    sumCum += element
                    cumSum.append(sumCum)
                #now compes the last step of using a sortedlist to find the closest match 
                ans = -math.inf 
                sortList = SortedList([]) #creating an empty sortedList 
                for element in cumSum:
                    if element > ans and element <= k: 
                        ans = element
                    if sortList:
                        ind = sortList.bisect_left(element-k)
                        if ind != len(sortList):
                            if element - sortList[ind] > ans and element - sortList[ind] <= k: #what if ind is out of range??? - it implies we have exceed for all 
                                ans = element - sortList[ind]
                    answers.append(ans)
                    sortList.add(element)
              
        return max(answers)
                
test = Solution()
matrix = [[1,0,1],[0,-2,3]]
k = 2 
print(test.maxSumSubmatrix(matrix,k))