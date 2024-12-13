#This code works just fine however the method of logging routes might not be the most efficient because it passes a new list everytime 
from collections import deque
from typing import Optional
import time 

class Solution:
    def __init__(self):
        self.allroutes = []
        self.adj_list = {}
        self.visited = {}
        self.depth = 0 

    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        ladder_start = time.time()
        word_dict = {i for i in wordList}
        if endWord not in word_dict:
            return None 
        if beginWord not in word_dict:
            wordList = wordList + [beginWord]
        self.adj_list = self.generate_adj_list(wordList)
        if beginWord not in self.adj_list:
            return None 
        self.depth = self.findDepth(beginWord,endWord,self.adj_list)
        if self.depth == None: 
            return []
        #print(self.visited)
        #print(self.depth)
        self.logRoutes([endWord],beginWord, self.depth-1)
        ladder_end = time.time()
        #print("ladder time = ",ladder_end-ladder_start,'s')
        return self.allroutes
        
    def logRoutes(self, route: list[str], endWord: str,  depth: int):
        if depth == 0:
            if endWord in self.adj_list[route[-1]]:
                route.append(endWord)
                self.allroutes.append(route[::-1])
                return 
        else: 
            for word in self.adj_list[route[-1]]:
                if word in self.visited[depth]:
                    self.logRoutes(route+[word],endWord,depth-1)

    def findDepth(self, beginWord: str, endWord: str, adj_list: list[str]) -> Optional[int]:
        visited = set()
        visited.add(beginWord)
        #self.visited[1] = {beginWord}
        queue = deque()
        queue.append((beginWord,1))
        while queue: 
            curr,curr_depth = queue.popleft()
            for vertex in adj_list[curr]:
                if vertex not in visited and vertex != endWord: 
                    queue.append((vertex,curr_depth+1))
                    visited.add(vertex)
                    if curr_depth in self.visited: 
                        self.visited[curr_depth].add(vertex)
                    else: 
                        self.visited[curr_depth] = {vertex}
                if vertex == endWord:
                    if curr_depth in self.visited: 
                        self.visited[curr_depth].add(vertex)
                    else: 
                        self.visited[curr_depth] = {vertex}
                    return curr_depth

    def generate_adj_list(self, wordList: list[str]) -> dict[str:list[str]]:
        adj_start = time.time()
        adj_list = {}
        all_words = {i for i in wordList}
        for word in wordList:
            check_dict = self.generate_dict(word)
            for word2 in check_dict: 
                if word2 in all_words:
                    if word in adj_list:
                        adj_list[word].add(word2)
                    else: 
                        adj_list[word] = set()
                        adj_list[word].add(word2)
        adj_end = time.time()
        print("adj_list_time = ",adj_end - adj_start,'s')
        return adj_list


    def generate_dict(self, word: str) -> dict[str]: 
        my_dict = set()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            left = word[0:i]
            right = word[i+1::]
            for center in alphabet:
                if center != word[i]:
                    my_dict.add(left+center+right)
        return my_dict