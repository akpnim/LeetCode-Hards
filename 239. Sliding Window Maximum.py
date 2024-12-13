import heapq
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        brain = {}
        myheap = [-1*nums[i] for i in range(k)]
        heapq.heapify(myheap)
        ans = []
        for i in range(k):
            if nums[i] not in brain: 
                brain[nums[i]] = 1 
            else: 
                brain[nums[i]] += 1 
        maxval = -1*myheap[0]
        ans.append(maxval)
        queue = deque([i for i in nums])
        for i in range(len(nums) - k):
            #print("here")
            out = queue.popleft()
            nextin = nums[i+k]
            heapq.heappush(myheap,-1*nextin)
            brain[out] -= 1 
            if nextin in brain: 
                brain[nextin] += 1 
            else: 
                brain[nextin] = 1 
            if nextin >= maxval: 
                maxval = nextin
            
            if out == maxval and brain[out] == 0: 
                max_found = False 
                while not max_found:
                    cand = -1*heapq.heappop(myheap)
                    #print("candidate= ", cand,brain)
                    if cand in brain: 
                        if brain[cand] > 0:
                            maxval = cand 
                            max_found = True 
            ans.append(maxval)
        return ans 

test = Solution()
nums = [1,2,1,0,0,0]
print(test.maxSlidingWindow(nums,2))
        