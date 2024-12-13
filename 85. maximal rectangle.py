class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        histograms = self.getHeights(matrix)
        max_area = 0 
        for histogram in histograms:
            if self.largestRectangleArea(histogram) > max_area:
                max_area = self.largestRectangleArea(histogram)
        return max_area
    
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
    
    def getHeights(self, matrix: list[list[str]]) -> list[list[int]]:
        heights = [[] for i in range(len(matrix[0]))] #number of histograms is the same as length of rows 
        cumsums = []
        for row in matrix: 
            cumsum = []
            runsum = 0 
            for element in row:
                if element == '1':
                    runsum += 1
                    cumsum.append(runsum)
                elif element == '0':
                    runsum = 0 
                    cumsum.append(runsum)
            cumsums.append(cumsum)

        #print(cumsums)
        for calcs in cumsums: 
            for i,calc in enumerate(calcs): 
                heights[i].append(calc)
        #print(heights)
        return heights

test = Solution()
matrix = [["1"]]
ans = test.maximalRectangle(matrix)
print(ans)
