# Definition for singly-linked list. The basic appraoch is a three step approach 
#First step is to add to chain the minimum from the heap 
#Second step is to add to heap the next from the current one in chain if it exists 
#Third step is to set the next from chain to None 

#The solution below is accepted 

import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]):
        #edge cases 
        if lists == [] or lists == [[]] or lists == [None]*len(lists):
            return None
        #initializing the main_chain and retaining a copy in order to return the head at the end 
        chain = ListNode()
        copy = chain 
        #initializing the minheap and heapifying the nodes with node.val as the parameter 
        our_heap = []
        our_dict = {} #using this to store the nodes 
        for node in lists: 
            if node: 
                our_heap.append(node.val)
                if node.val in our_dict:
                    our_dict[node.val].append(node)
                else: 
                    our_dict[node.val] = [node]

        heapq.heapify(our_heap)
        #onto the main section which executes while heap exists
        while our_heap:
            newcomer = our_dict[heapq.heappop(our_heap)].pop()
            #step 1 - adding to chain the minimum from heap
            chain.next = newcomer
            #step 2 - adding to heap the next one from chain 
            if newcomer.next: 
                heapq.heappush(our_heap,newcomer.next.val)
                if newcomer.next.val in our_dict:
                    our_dict[newcomer.next.val].append(newcomer.next)
                else: 
                    our_dict[newcomer.next.val] = [newcomer.next]
                    #Step 3 - is to set the next from chain to none 
                newcomer.next = None 
            chain = chain.next
        return copy.next
        