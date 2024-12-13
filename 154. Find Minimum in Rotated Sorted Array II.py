class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = self.findMin(nums[:len(nums)//2]), self.findMin(nums[len(nums)//2::])
        return min(left,right)

test = Solution()
testcase = [3,1,3] #this counterexample proves the above code wrong...