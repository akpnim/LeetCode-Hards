#Step 1: move either left or right one step and Declare newVal, update leftmax or rightmax as well 
#Step 2: calculate min(leftmax, rightmax) - newVal; if ans >0: totals += ans
class Solution: 
    def trap(self, heights: list[int]) -> int: 
        left, right = 0, len(heights)-1 
        leftmax, rightmax = heights[left], heights[right]
        ans = 0 
        while right -left > 1: 
            #Step 1 
            if heights[left] <= heights[right]:
                left += 1 
                newVal = heights[left]
                if newVal > leftmax:
                    leftmax = newVal
            
            else: 
                right -= 1 
                newVal = heights[right]
                if newVal > rightmax: 
                    rightmax = newVal
            
            #Step 2
            calculation = min(leftmax,rightmax) - newVal 
            if calculation > 0: 
                ans += calculation
        
        return ans 

test = Solution()
heights = [1,2,3,4,3,2,1,10]
print(test.calculateTrap(heights))
            
