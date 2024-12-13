from collections import deque

class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root == None: 
            return "None"
        worq = deque([root])
        ans = [root.val]#initializing ans with root.val  
        while worq:
            curnode = worq.popleft()
            leftnode = curnode.left
            rightnode = curnode.right
            if leftnode == None: 
                ans.append(None)
            else: 
                ans.append(leftnode.val)
                worq.append(leftnode)
              

            if rightnode == None: 
                ans.append(None)
            else:
                ans.append(rightnode.val)
                worq.append(rightnode)
         
        return str(ans) 
            
        

    def deserialize(self, data): #checked code - only thing to check is if we need to do a deepcopy to store ans...
        if data == "None":
            return None 
        data = eval(data) #converts to a list format 
        data = deque(data)#converst to a dequeue
        worq = deque([data.popleft()]) #creates a new working queue initialized with the root 
        curnode = None #initializing a rootnode for easy assingment during while looop 
        ans = None
        while data:
            if curnode == None: 
                curnode = TreeNode(worq.popleft()) #initializing rootnode if it doesnt exist 
                ans = curnode #storing in ans for later retrieval during return
            else: 
                curnode = worq.popleft()

            leftval = data.popleft()
            rightval = data.popleft()
            if leftval != None: 
                curnode.left = TreeNode(leftval)
                worq.append(curnode.left)
            else: 
                curnode.left = None 
            if rightval!= None: 
                curnode.right = TreeNode(rightval)
                worq.append(curnode.right)
            else: 
                curnode.right = None 
        return ans 

test = Codec()
data = "[1,2,3,None,None,4,5]"
ourtree = test.deserialize(data) #should return the root of the final tree 
ourstring = test.serialize(ourtree)
print(ourstring)
