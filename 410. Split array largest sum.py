#The below solution uses binary search on the solution space! Very good problem - simple and elegent solution!!!

import heapq, math 
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low != high:
            mid = (low + high)//2 
            print(low, high, mid)
            summ = 0 
            count = 0 
            for num in nums:
                if summ + num > mid:
                    count += 1 
                    summ = num  
                else: 
                    summ += num 

            count += 1 

            if count > k: #this means that our mid value is too low and we need to increase our mid value to accomodate more numbers per subarray
                low = mid + 1 
            else: 
                high = mid 
 
        return low #low == high == mid == ans: The answer converges here 
        
test = Solution()
nums = [7,2,5,10,8]
k = 2 
#expected 194890
print(test.splitArray(nums,k))