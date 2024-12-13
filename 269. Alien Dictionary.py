class Solution:
    def __init__(self):
        self.visited = {}
        self.adjlist = None 
        self.v = None 
    def alienOrder(self, words: list[str]) -> str:
        #First lets extract how many alphabets appear in our list of words
        count = set()
        for word in words: 
            for char in word: 
                count.add(char)
        self.v = len(count)
        if self.v == 1:
            return [i for i in count][0]
        #Now lets build the adjacency dict 
        adj_dict = {}
        for i in range(len(words)-1):
            for j,letter in enumerate(words[i]):
                if j >= len(words[i+1]):
                    return "" 
                if letter != words[i+1][j]:
                    if letter in adj_dict:
                        adj_dict[letter].append(words[i+1][j])
                    else:
                        adj_dict[letter] = [words[i+1][j]]
                    break 
        self.adjlist = adj_dict
        print(self.adjlist)
        #now onto the main part 
        for source in adj_dict:
            if source not in self.visited:
                a = self.dfs(source,set())
                if a =="":
                    return ""
        #now lets return the format needed
        print(self.visited)
        inconclusive = count.difference(self.visited)
        print(inconclusive)
        ans = ""
        for char in inconclusive:
            ans += char 
        rev_dict = {self.visited[key]:key for key in self.visited} 
        for i in range(len(inconclusive)+1,len(rev_dict)+len(inconclusive)+1):
            ans += rev_dict[i]
        return ans 
    
    def dfs(self, vertex: str, stack:set):
        print("vertex = ",vertex, "stack = ",stack)
        if vertex in self.adjlist:
            for neighbor in self.adjlist[vertex]:
                if neighbor not in self.visited and neighbor not in stack:
                    a = self.dfs(neighbor,stack.union({vertex}))
                    if a == "":
                        return ""
                elif neighbor in stack: 
                    print("here")
                    return ""
        
        if vertex not in self.visited: 
            self.visited[vertex] = self.v
            self.v -= 1 
        
        elif self.visited[vertex] == None:
            return ""

test = Solution()
#words = ["wrt","wrf","er","ett","rftt"]
words = ["zy","zx"]

print(test.alienOrder(words))