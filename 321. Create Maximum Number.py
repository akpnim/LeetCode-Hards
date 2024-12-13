import math 
class Solution:
    def __init__(self):
        self.nums1 = None 
        self.nums2 = None 

    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        self.nums1 = nums1 
        self.nums2 = nums2 
        ans = []
        for i in range(k+1):
            k1 = i 
            k2 = k-i 
            pro = self.generator(k1,k2)
            print(pro)
            if pro != (None, None):
                ans.append(self.combinator(pro[0],pro[1]))
        maxind = -1 
        maxval =  -math.inf
        for i,value in enumerate(ans):
            if int(value) > maxval:
                maxval = int(value)
                maxind = i 
        #print(ans)
        ans = ans[maxind]
        finans = []
        for dig in ans: 
            finans.append(int(dig))
        return finans

    def generator(self, k1:int, k2:int) -> tuple: 
        if len(self.nums1) < k1 or len(self.nums2) < k2: 
            return (None, None)
        ans1 = []
        ans2 = [] 
        tempdict1 = set()
        prev1 = -1
        prev2 = -1 
        tempdict2 = set()
        lp= 0
        rp = len(self.nums1) - k1 
        while rp!= len(self.nums1):
            maxi = -math.inf
            ind = -1 
            for i in range(lp,rp+1):
                if self.nums1[i] > maxi and i not in tempdict1 and i>prev1:
                    maxi = self.nums1[i]
                    ind = i 
            prev1 = ind 
            tempdict1.add(ind)
            ans1.append(self.nums1[ind])
            rp = rp+1
            lp = lp+1
        lp= 0
        rp = len(self.nums2) - k2
        while rp!= len(self.nums2):
            maxi = -math.inf
            ind = -1 
            for i in range(lp,rp+1):
                if self.nums2[i] > maxi and i not in tempdict2 and i>prev2:
                    maxi = self.nums2[i]
                    ind = i 
            prev2 = ind 
            tempdict2.add(ind)
            ans2.append(self.nums2[ind])
            rp = rp+1
            lp = lp+1
        return (ans1,ans2)
    
    def combinator(self, nums1: list[int], nums2: list[int]) -> str: 
        lp,rp = 0,0
        ans = [] 
        while lp<len(nums1) and rp< len(nums2):
            if nums1[lp] > nums2[rp]:
                ans.append(nums1[lp])
                lp = lp + 1 
            elif nums1[lp] < nums2[rp]:
                ans.append(nums2[rp])
                rp = rp + 1 
            elif nums1[lp] == nums2[rp]:
                verdict = self.lexCompare(nums1[lp::],nums2[rp::])
                if verdict == 1: 
                    ans.append(nums1[lp])
                    lp = lp + 1 
                elif verdict == 2: 
                    ans.append(nums2[rp])
                    rp = rp + 1 

        if lp == len(nums1) and rp == len(nums2):
            return ans 
        
        elif lp == len(nums1):
            while rp < len(nums2):
                ans.append(nums2[rp])
                rp = rp + 1 
        elif rp == len(nums2):
            while lp < len(nums1):
                ans.append(nums1[lp])
                lp = lp + 1 
        finans = ""
        for dig in ans: 
            finans += str(dig)
        return finans

    def lexCompare(self, nums1:list[int], nums2: list[int]) -> int: #if it returns 0, then pick nums1 and if it returns 1, pick nums2
        comp1 = nums1 
        comp2 = nums2
        i = 0 
        if len(nums1) > len(nums2):
            k = math.ceil(len(nums1)/len(nums2))
            comp2 = comp2*k
        elif len(nums2) > len(nums1):
            k = math.ceil(len(nums2)/len(nums1))
            comp1 = comp1*k
        
        while comp1[i] == comp2[i]:
            i = i + 1 
            if i>= len(comp1) or i>= len(comp2):
                if len(nums1) > len(nums2):
                    return 1 
                else: 
                    return 2 
            if comp1[i] > comp2[i]:
                return 1 
            elif comp1[i] < comp2[i]:
                return 2 



test = Solution()
nums1 = [8,1,8,8,6]
nums2 = [4]
print(test.maxNumber(nums1,nums2,2))