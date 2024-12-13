import math 

class Solution:
    def binary_search(self, num1: list[int] ,ceiling: float):

        count = 0 #to be returned at the end 
        #base case 
        if len(num1) == 1:
            if num1[0] <= ceiling: 
                return 1
            else:
                return 0 
            
        if len(num1) == 0: 
            return 0
            
        #calculating the median - consider using a separate function for this 
        med = self.median(num1)

        #assigning the median index to aid in splitting the array in both odd and even cases 
        median_index = None 
        if len(num1)%2 == 0: 
            median_index = len(num1)//2 -1
        elif len(num1)%2 != 0: 
            median_index = len(num1)//2 

        if med <= ceiling:  
            count += median_index + 1 
            count = count + self.binary_search(num1[median_index+1::],ceiling)
        if med > ceiling: 
            count = count + self.binary_search(num1[0:median_index+1],ceiling)
        
        return count 


    def median(self, nums1: list[int]) -> float: 
        if len(nums1) == 0: 
            return ValueError
        if len(nums1) == 1:
            return nums1[0]
        if len(nums1)%2 != 0: 
            return nums1[len(nums1)//2]
        elif len(nums1)%2 == 0: 
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2 

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) == 1 and len(nums2) == 1: 
            return (nums1[0] + nums2[0])/2
        
        if len(nums1) == 0 and len(nums2) != 0: 
            return self.median(nums2)
        
        if len(nums2) == 0 and len(nums1) != 0: 
            return self.median(nums1)
        
        n = len(nums1) #length of nums1 
        m = len(nums2) #lenfth of nums2 
        len_median = (n+m)//2 + 1 #counts the number of total elements we care about 
        smaller_count = 0 #counts the number of elements to use from this array 
        larger_count = 0 #counts the number of elements to use from this array 
        smaller = [] #the array with the smaller median 
        larger = [] #the array with the larger median 
        med1 = None #median of array num1 
        med2 = None #median of array num2 
        #basically the below counts are guaranteed for the array with a smaller median 

        med1 = self.median(nums1)
        med2 = self.median(nums2)

        if med1 <= med2:
            smaller_count = n//2 - 1 
            smaller,larger = nums1,nums2
            if len(smaller)%2 !=0: 
                smaller_count += 1  
        if med2 < med1:
            smaller_count = m//2 - 1 
            smaller, larger = nums2, nums1 
            if len(smaller)%2 != 0: 
                smaller_count += 1 
        
        #if len(nums1) == 1 and len(nums2) == 1: 
        #    return (nums1[0] + nums2[0])/2
            
        print (f"smaller_count = {smaller_count},larger_count = {larger_count},len_median = {len_median}")
               
        #entering the main loop
        
        counted = set()
        for ceiling in smaller[smaller_count::]: 
            if ceiling not in counted: 
                count = self.binary_search(larger[larger_count::],ceiling)
                larger_count += count
                counted.add(ceiling)
            if larger_count + smaller_count >= len_median:
                print(f"counted = {counted}")
                print(f"small_count = {smaller_count}; large_count = {larger_count}")
                break 

            smaller_count += 1 
            print(f"counted = {counted}")
            print(f"small_count = {smaller_count}; large_count = {larger_count}")
            print(f"len_median = {len_median}")
        
        if smaller_count + larger_count != len_median:
            larger_count = len_median - smaller_count

        ans = None

        if (len(smaller) + len(larger))%2 == 0: 
            candidates = [smaller[smaller_count-1]]
            if smaller_count >= 2: 
                candidates.append(smaller[smaller_count-2])
            if larger_count >= 1: 
                candidates.append(larger[larger_count-1])
            if larger_count >= 2: 
                candidates.append(larger[larger_count-2])
            answer_array = sorted(candidates)[::-1]
            ans = (answer_array[0] + answer_array[1])/2
        
        elif (len(smaller)+ len(larger))%2 !=0: 
            candidates = [smaller[smaller_count-1]] 
            if larger_count >= 1: 
                candidates.append(larger[larger_count-1])
            answer_array = sorted(candidates)[::-1]
            ans = max(candidates)

        return ans 

    





a = Solution()
print(a.findMedianSortedArrays([1,2],[-1,3]))
        

