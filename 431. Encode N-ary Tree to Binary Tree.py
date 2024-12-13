from collections import deque 
# Definition for a Node for N-ary Tree
class Node:
    def __init__(self, val:int = None, children: list['Node'] = []):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') ->  TreeNode: 
        if root == None: 
            return None 
        q = deque([root])
        ans = TreeNode(root.val) 
        mydict = {root:ans}
        while q: 
            curnary = q.popleft()
            currbin = mydict[curnary]
            for i,child in enumerate(curnary.children):
                q.append(child)
                if i == 0: 
                    currbin.left = TreeNode(child.val)
                    currbin = currbin.left
                else: 
                    currbin.right = TreeNode(child.val)
                    currbin = currbin.right
                mydict[child] = currbin #adding the 'child's binary tree node as the value of the dictionary with the n-ary node as the key 
        return ans
    
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> Node:
        if data == None: 
            return None 
        q = deque([data])
        ans = Node(data.val,[])
        mydict = {data: ans}
        while q: 
            curbin = q.popleft()
            curnary = mydict[curbin]
            if curbin.left:
                curbin = curbin.left 
                q.append(curbin)
                newnode = Node(curbin.val,[])
                curnary.children.append(newnode)
                mydict[curbin] = newnode  
                while curbin.right: 
                    curbin = curbin.right
                    navanode = Node(curbin.val,[])
                    curnary.children.append(navanode)
                    mydict[curbin] = navanode
                    q.append(curbin)
        return ans 
                

        