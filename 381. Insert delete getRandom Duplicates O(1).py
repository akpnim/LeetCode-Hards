#first we will implement the one with random not allwoed and then later the one with allowed
import random

class RandomizedCollection:

    def __init__(self):
        self.mydict = {}
        self.mylist = []
        
    def insert(self, val: int) -> bool:
        ans = True 
        if val in self.mydict:
            ans = False 
            self.mydict[val].add(len(self.mylist)) #remembering the index of val in mylist 
        
        else: 
            self.mydict[val] = {len(self.mylist)} #remembering the index of val in mylist 
        
        self.mylist.append(val) #adding the val at that index 
        return ans 

    def remove(self, val: int) -> bool: #I think I switched it around by mistake 
        if val in self.mydict:
            indexInList = self.mydict[val].pop()
            self.mylist[indexInList] = self.mylist[-1] #placing the last element here 
            self.mydict[self.mylist[-1]].add(indexInList) #updating the address of the last element 
            self.mydict[self.mylist[-1]].remove(len(self.mylist)-1)
            self.mylist.pop()
            if not self.mydict[val]:
                del self.mydict[val]
            return True 
        
        return False 

    def getRandom(self) -> int:
        ans = random.choice(self.mylist)
        return ans 

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()