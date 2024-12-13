class Solution:
    def __init__(self):
        self.cands = []
        self.visited = set()
        self.adjlist = {}
        self.length = 0
        self.tickets = None 
        self.brain = set()

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.tickets = tickets 
        self.length = len(tickets) + 1 
        for i,ticket in enumerate(tickets): 
            if ticket[0] in self.adjlist:
                self.adjlist[ticket[0]].append((ticket[1],i))
            else: 
                self.adjlist[ticket[0]] = [(ticket[1],i)]
        #print(self.adjlist)
        #print(self.adjlist["JFK"])
        self.dfs("JFK",["JFK"],"JFK")
        return sorted(self.cands)[0] 
    
    def dfs(self, origin: str, path: list[str], pathstr: str):
        if len(path) == self.length:
            self.cands.append([i for i in path])
            #print("cands=",self.cands)
            #print(pathstr)
            return True 
        
        if origin in self.adjlist:
            for addr in sorted(self.adjlist[origin]):
                if addr[1] not in self.visited and pathstr + '-' + addr[0] not in self.brain: 
                    self.visited.add(addr[1])
                    self.brain.add(pathstr + '-' + addr[0])
                    path.append(addr[0])
                    a = self.dfs(addr[0],path, pathstr + '-' + addr[0])
                    if a == True: 
                        return True 
                    path.pop()
                    self.visited.remove(addr[1])
        return 

test = Solution()
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(test.findItinerary(tickets))
