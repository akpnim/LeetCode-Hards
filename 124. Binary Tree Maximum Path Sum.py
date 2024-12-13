# Definition for a binary tree node.
import math 
from typing import Optional 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def __init__ (self):
        #self.maxroot = TreeNode(-10000)
        self.maxval = -math.inf
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calc_max(root)
        return self.maxval

    def calc_max(self, root) -> int:
        if root == None: 
            return -math.inf
        p_left = self.calc_max(root.left)
        p_right = self.calc_max(root.right)
        max_possible = self.maxSumThree([p_left,root.val,p_right])
        if max_possible > self.maxval:
            #self.maxroot = root
            self.maxval = max_possible
        if p_left > 0 or p_right>0: 
            return max(p_left, p_right) + root.val 
        else: 
            return root.val 

    
    def maxSumThree(self, s: list[int]) -> int: 
        if s[0] >=0 and s[2] >=  0: 
            return sum(s)
        elif s[0] < 0 and s[2] < 0: 
            return s[1]
        elif s[0] < 0 or s[2] < 0: 
            return s[1] + max(s[0],s[2])
    
