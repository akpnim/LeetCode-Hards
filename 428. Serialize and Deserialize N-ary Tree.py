from collections import deque 
# Definition for a Node.
class Node(object):
    def __init__(self, val: int = None, children: list['Node'] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root: Node) -> str:
        if root == None: #base case 
            return "[]"
        #initializing the structures 
        ans = [root.val, None]
        q = deque([root])

        while q: 
            curr = q.popleft()
            if curr.children: 
                for child in curr.children:
                    q.append(child)
                    ans.append(child.val)
                ans.append(None)
            else: 
                ans.append(None)

        while ans[-1] == None:
            ans.pop() #removing the last none 
        print(ans)
        return str(ans)
    
        
	
    def deserialize(self, data: str) -> 'Node':
        data = eval(data)
        if not data: 
            return None 
        position = 1 
        ans = Node(data[0])
        q = deque([ans])
        while position < len(data):
            if data[position] == None: 
                curr = q.popleft()
                position += 1 
            else:
                child = Node(data[position]) 
                curr.children.append(child)
                q.append(child)
                position += 1 

        return ans 
                
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))