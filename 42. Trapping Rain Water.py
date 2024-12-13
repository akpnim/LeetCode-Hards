#here we used a helper function to optimize memory instead of using recursion directly 

class Solution:
    def trap(self, height: list[int]) -> int:
        return self.helper(height,0)

    def helper(self,height, start):
        if len(height) <=2: 
            return 0 
        first_index = -1 
        first_element = -1
        for i in range(start,len(height)):
            if height[i] != 0: 
                first_index = i 
                first_element = height[i] 
                break 
        if first_index == -1: 
            return 0 
        
        max_element = -1 
        max_index = -1 
        for i in range(first_index+1,len(height)):
            if height[i] >= max_element: 
                max_index = i 
                max_element = height[i] 
            if height[i] > first_element:
                break 
        
        lower_height = min(height[first_index],height[max_index])
        total = 0 
        for i in range(first_index+1,max_index):
            total += lower_height - height[i]
            
        #now that we have found the max and the first, we have to calculate 
        return total + self.helper(height,max_index)
        
    
    

test = Solution()
testcase = [0,1,0,2,1,0,1,3,2,1,2,1]

print(test.trap(testcase))
