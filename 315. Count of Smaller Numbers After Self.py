from collections import deque 

class Solution:
    def __init__(self):
        self.ans = None 


    def countSmaller(self, nums: list[int]) -> list[int]:
        self.ans = [len(nums)-i-1 for i in range(len(nums))]
        nums = [(nums[i],i) for i in range(len(nums))]
        self.mergeSort(nums)
        return self.ans 

    def mergeSort(self,nums: list[tuple[int]]) -> list[tuple[int]]:
        if len(nums) == 1: 
            return nums 
        
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2::]
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        left = deque(left)
        right = deque(right)
        ans = []
        cross = 0 
        while left: 
            if not right: 
                while left:
                    to_add = deque.popleft(left)
                    self.ans[to_add[1]] -= cross 
                    ans.append(to_add)
                continue

            if left[0] > right[0]:
                to_add = deque.popleft(left)
                self.ans[to_add[1]] -= cross 
                ans.append(to_add)
                continue
            else: 
                to_add = deque.popleft(right)
                cross += 1 
                ans.append(to_add)

        while right:
            ans.append(deque.popleft(right))

        return ans 
    
test = Solution() 
print(test.countSmaller([-1,-1]))
