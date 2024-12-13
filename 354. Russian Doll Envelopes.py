class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        sorted_envelopes = self.customSort(envelopes)
        y_list = [val[1] for val in sorted_envelopes]
        stack = []
        for num in y_list: 
            pos = self.binSearch(num,stack)
            if pos == -1: 
                stack.append(num)
            else: 
                stack[pos] = num 

        return len(stack)

#custom binary search to suit our needs
    def binSearch(self, num: int, stack: list[int]) -> int:
        if not stack:
            return -1
        
        elif num > stack[-1]:
            return -1 
        
        elif num <= stack[0]:
            return 0 
        
        else: 
            left = 0 
            right = len(stack) - 1 
            while right - left != 1: 
                mid = (right + left) // 2 
                if num <= stack[mid]:
                    right = mid 
                elif num > stack[mid]:
                    left = mid 

            return right 



    def customSort(self, envelopes: list[list[int]]) -> list[list[int]]: 
        if len(envelopes) == 1: #base case 
            return envelopes
        
        index = len(envelopes)//2 
        left = envelopes[:index]
        right = envelopes[index::]
        left = self.customSort(left)
        right = self.customSort(right)

        ans = [] 
        l,r = 0,0 
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                ans.append(left[l])
                l+=1 
            elif right[r][0] < left[l][0]:
                ans.append(right[r])
                r+=1 
            elif left[l][0] == right[r][0]:
                if left[l][1] < right[r][1]:
                    ans.append(right[r])
                    r+=1 
                elif right[r][1] < left[l][1]:
                    ans.append(left[l])
                    l+=1 
                else: 
                    ans.append(left[l])
                    l+=1 
        
        while l<len(left):
            ans.append(left[l])
            l+=1 
        
        while r<len(right):
            ans.append(right[r])
            r+=1 

        return ans 


test = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes2 = [[1,1],[1,1],[1,1]]
envelopes3 = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
print(test.maxEnvelopes(envelopes3))
