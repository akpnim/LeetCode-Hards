# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        if head == None: 
            return None 
        copy = head 
        for i in range(k-1):
            if head.next:
                head = head.next
            else: 
                return copy 
        agla = head.next 
        head.next = None 
        A = self.rev_list(copy)
        for i in range(k-1):
            A = A.next 
        A.next = self.reverseKGroup(agla,k)
        return head 
    
   
    def rev_list(self,head):
        if head.next == None:  
            return head 
        newHead = self.rev_list(head.next)
        if head.next.next == None: 
            head.next.next = head 
            head.next = None 
        return newHead
    