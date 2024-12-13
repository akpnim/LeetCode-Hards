class AllOne:
    def __init__(self):
        self.mydict = {}
        self.revdict = {}

    def inc(self, key: str) -> None:
        if key in self.mydict:
            self.revdict[self.mydict[key]].remove(key)
            if not self.revdict[self.mydict[key]]:
                del self.revdict[self.mydict[key]]
            self.mydict[key] += 1 
            if self.mydict[key] in self.revdict:
                self.revdict[self.mydict[key]].add(key)
            else:
                self.revdict[self.mydict[key]] = set()
                self.revdict[self.mydict[key]].add(key)
        
        else: 
            self.mydict[key] = 1 
            if self.mydict[key] in self.revdict:
                self.revdict[self.mydict[key]].add(key)
            else:
                self.revdict[self.mydict[key]] = set()
                self.revdict[self.mydict[key]].add(key)

    def dec(self, key: str) -> None:
        self.revdict[self.mydict[key]].remove(key)
        if not self.revdict[self.mydict[key]]:
            del self.revdict[self.mydict[key]]

        self.mydict[key] -= 1 
        
        if self.mydict[key] == 0:
            del self.mydict[key]
            return 

        if self.mydict[key] in self.revdict:
            self.revdict[self.mydict[key]].add(key)
        else:
            self.revdict[self.mydict[key]] = set()
            self.revdict[self.mydict[key]].add(key)

    def getMaxKey(self) -> str:
        #print(self.revdict)
        if self.revdict:
            maxx = max(self.revdict)
            for element in self.revdict[maxx]:
                return element 
        return ""

    def getMinKey(self) -> str:
        #print(self.revdict)
        if self.revdict:
            minn = min(self.revdict)
            for element in self.revdict[minn]:
                return element     
        
        return ""