import heapq, math 
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or k == 1: 
            return s 
        
        mydict = {}
        for char in s: 
            if char in mydict:
                mydict[char] += 1 
            else: 
                mydict[char] = 1
        
        heap = []
        for key in mydict:
            heap.append([-mydict[key],key])
        heapq.heapify(heap)
        ans = ""
        working = []
        while True: 
            for i in range(k):
                if heap:
                    working.append(heapq.heappop(heap))
           
            broken = k
            
            for i in range(len(working)):
                if len(working) < k and -1*working[i][0] > 1: 
                    return ""
                
                ans += working[i][1]
                working[i][0] += 1 

                if working[i][0] == 0 and broken == k: 
                    broken = i 

            if broken == 0 and not heap: 
                return ans 
            
            
            for ele in working[:broken]:
                heapq.heappush(heap,ele)
                
            working = []




test = Solution()
s = "aabbcc"
k = 3
ans = test.rearrangeString(s,k)
print(ans)

        
