#first lets implement Left to Right
#buildings[i] = [lefti,righti,heighti]; remember that appending to the maxheap should be in the form (heighti, lefti, righti)
import heapq 
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        heap = []
        leftans = []
        heapq.heapify(heap)
        #first left to right 
        for buil in buildings: 
            if heap: 
                while heap[0][1][1] < buil[0] and heap: #if building terminates before current building 
                    heapq.heappop(heap)
                    if not heap: 
                        break 
            if not heap: #basically no chance of collision
                heapq.heappush(heap,[-1*buil[2],buil])
                leftans.append([buil[0],buil[2]])
                continue
            elif -1*heap[0][0] >= buil[2] and heap[0][1][1] >= buil[0]: #if prev building is taller and crosses current one 
                heapq.heappush(heap,[-1*buil[2],buil])
                continue 
            elif -1*heap[0][0] < buil[2] and heap[0][1][1] >= buil[0]: #if prev building is shorter and crosses current one 
                heapq.heappush(heap,[-1*buil[2],buil])
                leftans.append([buil[0],buil[2]])
        #now right to left - logic is the same however when we add to ans we add the "lower" point not the higher one. first need to sort by righti
        buildings = sorted(buildings,key= lambda coor: coor[1])
        heap = []
        rightans = []
        heapq.heapify(heap)
        for buil in buildings[::-1]:
            if heap: 
                while heap[0][1][0] > buil[1] and heap: #if building terminates before current building 
                    heapq.heappop(heap)
                    if not heap: 
                        break 
            if not heap: #basically no chance of collision
                heapq.heappush(heap,[-1*buil[2],buil])
                rightans.append([buil[1],0])
                continue

            elif -1*heap[0][0] >= buil[2] and heap[0][1][0] <= buil[1]: #if prev building is taller and crosses current one 
                heapq.heappush(heap,[-1*buil[2],buil])
                continue 

            elif -1*heap[0][0] < buil[2] and heap[0][1][0] <= buil[1]: #if prev building is shorter and crosses current one 
                rightans.append([buil[1],heap[0][1][2]])
                heapq.heappush(heap,[-1*buil[2],buil])
     
        leftans= sorted(leftans)
        leftansdict = {}
        for coor in leftans: 
            leftansdict[coor[0]] = coor[1]
        leftans = []
        for key in leftansdict: 
            leftans.append([key,leftansdict[key]])
        
        rightans= sorted(rightans)
        rightansdict = {}
        for coor in rightans: 
            if coor[0] not in rightansdict:
                rightansdict[coor[0]] = coor[1]
        rightans = []
        for key in rightansdict: 
            rightans.append([key,rightansdict[key]])

        ans = leftans + rightans 
        ans = sorted(ans)
        return ans 
    

test = Solution()
buildings = [[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]

print(test.getSkyline(buildings))

