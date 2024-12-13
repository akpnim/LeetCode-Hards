import math 
class Solution:
    def candy(self, ratings: list[int]) -> int:
        ans = 0 
        brain = {}
        indices = sorted(range(len(ratings)), key= lambda x: ratings[x])
        for index in indices: 
            left,right = -math.inf, -math.inf
            curr, currind = None, None 
            if index - 1 in brain: 
                left = brain[index - 1]
                curr = left
                currind = index - 1 
            if index + 1 in brain: 
                right = brain[index+1]
                if right > left:
                    curr = right 
                    currind = index + 1 
            if curr == None: 
                brain[index] = 1 
                ans += 1
                continue 
            if ratings[index] > ratings[currind]:
                brain[index] = curr + 1 
                ans += curr + 1 
                continue 
            elif ratings[index] == ratings[currind] and right == left: 
                brain[index] = curr + 1 
                ans += curr + 1 
                continue
            if ratings[index] == ratings[currind]: 
                if right== -math.inf or left == -math.inf:
                     brain[index] = 1 
                     ans += 1 
                     continue
                
                else: 
                    minimuim = min(left,right)
                    brain[index] = minimuim + 1 
                    ans += minimuim + 1 
                    continue 
            else: 
                brain[index] = 1
                ans += 1

        return ans 


test = Solution()
s = [1,2,4,4,3]
#s = [29,51,87,87,72,12]
print(test.candy(s))

import math 
class Solution:
    def candy(self, ratings: list[int]) -> int:
        toright = []
        toleft = []
        toright.append(1)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                toright.append(toright[-1] + 1)
            else: 
                toright.append(1)
        toleft.append(1)
        for i in range(len(ratings)-1)[::-1]:
            if ratings[i] > ratings[i+1]:
                toleft.append(toleft[-1]+1)
            else: 
                toleft.append(1)
        maxies = []
        toleft = toleft[::-1]
        for i in range(len(toleft)):
            maxies.append(max(toleft[i],toright[i]))
        return sum(maxies)


test = Solution()
s = [1,0,2]
#s = [29,51,87,87,72,12]
print(test.candy(s))