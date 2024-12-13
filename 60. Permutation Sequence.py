import time 
start = time.time()

import math 

class Solution:
    def __init__(self):
        self.allPermutations = []

    def getPermutation(self, n: int, k: int) -> str:
        
        n_list = [str(i) for i in range(1,n+1)]
        if n_list == []:
            return []
        if len(n_list) == 1: 
            if n==1: 
                self.allPermutations.append(n_list[0]) 
            return n_list[0]
        elif len(n_list) == 2:
            if n == 2: 
                self.allPermutations.append(n_list[0]+n_list[1])
                self.allPermutations.append(n_list[1]+n_list[0])
            return self.allPermutations[k-1]
        
        left_list = []
        right_list = []
        for i,left in enumerate(n_list): 
            left_list.append(left)
            right = n_list[0:i]+n_list[i+1::]
            right_list.append(right)
        left_index = math.ceil(k/math.factorial(n-1)) - 1 
        kth_index = k - (left_index+1)*math.factorial(n-1) - 1 
        first_char = left_list[left_index]
        n_list.remove(first_char)
        self.computePerm(n-1,n_list)
        print(self.allPermutations)
        return first_char+self.allPermutations[kth_index]
    
    def computePerm(self,n: int, n_list: list[str]) -> None:
        #base cases 
        if n_list == []:
            return []
        if len(n_list) == 1: 
            if n==1: 
                self.allPermutations.append(n_list[0]) 
            return [n_list[0]]
        elif len(n_list) == 2:
            if n == 2: 
                self.allPermutations.append(n_list[0]+n_list[1])
                self.allPermutations.append(n_list[1]+n_list[0])
            return [n_list[0]+n_list[1],n_list[1]+n_list[0]]
        #done ith base cases - lets move to the main code 
        left_list = []
        right_list = []
        for i,left in enumerate(n_list): 
            left_list.append(left)
            right = n_list[0:i]+n_list[i+1::]
            right_list.append(right)
        to_return = []
        for i,left in enumerate(left_list):
            a = self.computePerm(n,right_list[i])
            for stringg in a: 
                to_add = left + stringg 
                to_return.append(to_add)
        if len(to_return[0]) == n: 
            for element in to_return:
                self.allPermutations.append(element)
        return to_return
    

test = Solution()

print(test.getPermutation(3,3))
        
end = time.time()

print(end-start,'s')
        
