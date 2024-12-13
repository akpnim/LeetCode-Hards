class Solution:
    def __init__(self):
        self.brain = {}
        self.pads = None 
        self.nums = None 

    def maxCoins(self, nums: list[int]) -> int:
        if self.pads == None: 
            nums = [1] + nums + [1]
            self.pads = True 
            self.nums = nums 
        
        return self.recursive(0,len(self.nums)-1)
    
    def recursive(self, start: int, stop: int) -> int: 
        if (start,stop) in self.brain:
            return self.brain[(start,stop)]
        
        if stop-start+1 == 3: 
            self.brain[(start,stop)] = self.nums[start]*self.nums[stop]*self.nums[start+1]
            return self.brain[(start,stop)]
        
        candidates = []

        for i in range(start+1,stop):
            left = 0 
            if i> start+1: 
                left = self.recursive(start,i)
            right = 0 
            if i<stop-1: 
                right = self.recursive(i,stop)

            mid = self.nums[i]*self.nums[start]*self.nums[stop]

            candidates.append(left+right+mid)

        self.brain[(start,stop)] = max(candidates)
        return self.brain[(start,stop)]


test = Solution()

ans = test.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9])
#ans = test.maxCoins([3,1,5,8])
print(ans)
