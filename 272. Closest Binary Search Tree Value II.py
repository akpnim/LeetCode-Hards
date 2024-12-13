#first attempting the O(nlogn) solution - it is accepted!

from typing import Optional 
import math 
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = None 
        self.diff = []
        heapq.heapify(self.diff)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> list[int]:
        self.dfs(root,target)
        ans = []
        for i in range(k):
            toadd = heapq.heappop(self.diff)[1]
            ans.append(toadd)
        return ans 

    def dfs(self, root: Optional[TreeNode], target: float) -> int:
        diff = abs(target-root.val)
        heapq.heappush(self.diff,(diff,root.val))
        if root.left: 
            self.dfs(root.left,target)
        if root.right: 
            self.dfs(root.right,target)
        