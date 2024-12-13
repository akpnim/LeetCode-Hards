class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        if len(distance) < 4: 
            return False 
        
        i = 2 
        while distance[i] - distance[i-2] > 0: 
            i = i + 1 
            if i == len(distance):
                return False 
        print("i= ", i)
        partial = False 
        cond1 = i%2 == 0 and i>2 
        cond2 = i%2 != 0 and i > 3
        if cond1 or cond2: 
            diff = distance[i-2] - distance[i-4]
            if distance[i] >= diff: 
                partial = True 
        
        if i == 3: 
            if distance[i] == distance[i-2]:
                partial = True 
    
        print("partial = ", partial)
        
        if partial == True: 
            limit = distance[i-1] -distance[i-3]
        
        elif partial == False: 
            limit = distance[i-1]
        
        if i+1 < len(distance):
            if distance[i+1] >= limit:
                return True 
            i = i + 1 
        
        
        if i+1 < len(distance):
            i = i + 1 
            while distance[i] < distance[i-2]:
                i = i + 1 
                if i == len(distance):
                    return False 

        if i == len(distance) -1 :
            return False 

        else: 
            return True 

test = Solution()

distance = [1,1,3,2,1,1]

print(test.isSelfCrossing(distance))