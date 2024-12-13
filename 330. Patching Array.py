class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        total, finans, ans, i = 0,0,[], 0 
        while total < n and i < len(nums):
            if nums[i] - total > 1: 
                ans.append(total+1)
                finans += 1 
                total += total + 1 
            else: 
                ans.append(nums[i])
                total += nums[i]
                i += 1 
        while total < n: 
            ans.append(total+1)
            finans += 1 
            total += total + 1 
        return finans