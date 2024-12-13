#This problem boils down to finding the next smaller for each element AND finding the previous smaller element for each element 
#Once we have both the next smaller element and the previous smaller element, we just multiply each value by the difference to get each area. 
#This was a challenging problem to figure out on my own due to the understanding of monotonic stacks required. We use increasing monotonic stacks. 

#step 1: find the previous smaller element indices for each element 
#step 2: find the next smaller element indices for each element by inverting heights
#step 3: calculate areas based on results from step 1, step 2 and heights array. 


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] 
        left_indices = self.getPrevSmaller(heights)
        right_indices = self.getPrevSmaller(heights[::-1])
        right_indices = right_indices[::-1]
        for i,element in enumerate(right_indices):
            if element != -1: 
                right_indices[i] = len(heights) - 1 - element 
        
        #print(left_indices,right_indices)
        areas = 0
        for i,height in enumerate(heights): 
            if left_indices[i] == -1 and right_indices[i] == -1: 
                width = len(heights)
            elif left_indices[i] == -1: 
                width = right_indices[i]
            elif right_indices[i] == -1: 
                width = len(heights) - left_indices[i] - 1  
            else: 
                width = right_indices[i] - left_indices[i] - 1 

            if width*height > areas: 
                areas = width*height

        return areas 

    
    def getPrevSmaller(self, heights:list[int]) -> list[int]:
        stack = [] 
        prev = [] 
        for i,height in enumerate(heights):
            if stack:   
                while stack[-1][0] >= height: 
                        stack.pop()
                        if stack == []:
                            break 
                if stack == []: 
                    stack.append((height,i))
                    prev.append(-1)
                elif stack[-1][0] < height: 
                    prev.append(stack[-1][1])
                    stack.append((height,i))
            else: 
                stack.append((height,i))
                prev.append(-1)
        return prev 


test = Solution()

heights = [4,2,0,3,2,5]
print(test.largestRectangleArea(heights))