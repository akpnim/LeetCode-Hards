from collections import deque
from typing import Optional
import time 

class Solution:
    def __init__(self):
        self.adj_list = {}
        self.depth = 0 
        self.brain = {}

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> Optional[int]:
        main_start = time.time()
        word_dict = {i for i in wordList}
        if endWord not in word_dict:
            return 0 
        if beginWord not in word_dict:
            wordList = wordList + [beginWord]
        start = time.time()
        self.adj_list = self.generate_adj_list(wordList)
        end = time.time()
        if beginWord not in self.adj_list:
            return 0 
        self.depth = self.findDepth(beginWord,endWord,self.adj_list)
        if self.depth == None: 
            return 0
        main_end = time.time()
        return self.depth + 1 

    def findDepth(self, beginWord: str, endWord: str, adj_list: list[str]) -> Optional[int]:
        visited = set()
        visited.add(beginWord)
        queue = deque()
        queue.append((beginWord,1))
        while queue: 
            curr,curr_depth = queue.popleft()
            for vertex in adj_list[curr]:
                if vertex not in visited and vertex != endWord: 
                    queue.append((vertex,curr_depth+1))
                    visited.add(vertex)
                if vertex == endWord:
                    return curr_depth

    def generate_adj_list(self, wordList: list[str]) -> dict[str:list[str]]:
        adj_list = {}
        all_words = {i for i in wordList}
        for word in wordList:
            check_dict = self.generate_dict(word)
            for word2 in check_dict: 
                if word2 in all_words:
                    if word in adj_list:
                        adj_list[word].append(word2)
                    else: 
                        adj_list[word] = [word2]
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