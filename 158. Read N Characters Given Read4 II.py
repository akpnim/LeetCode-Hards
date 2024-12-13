# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
import math 

class Solution:
    def __init__(self):
        self.storage = ['']*4
        self.lastpos = 0
        self.prevmax = 0

    def read(self, buf: List[str], n: int) -> int:
        print("buf=",buf[:15])
        runtimes = math.ceil(n/4)
        i = 0 
        earlybreak = False 
        while runtimes>0:
            if self.storage != ['']*4:
                print(self.lastpos, "= self.lastpost")
                print(self.prevmax, "= self.prevmax")
                for j,char in enumerate(self.storage[self.lastpos:self.prevmax]):
                    buf[i]= self.storage[j+self.lastpos]
                    i += 1 
                    if i == n:
                        self.lastpos = j+self.lastpos+1
                        break 
            print("buf2=",buf[:15])
            if i==n: 
                if self.lastpos!= self.prevmax:
                    earlybreak = True 
                break 
            runtimes -= 1  
            a = read4(self.storage)
            print(self.storage)
            print("a=", a)
            for j in range(a):
                buf[i]= self.storage[j]
                i += 1 
                if i == n:
                    self.lastpos = j+1
                    self.prevmax = a
                    print(self.lastpos, self.prevmax,self.storage)
                    break 
            if i==n:
                earlybreak = True
                break 
            self.storage = ['']*4
            self.lastpos = 0
            self.prevmax = 0
        if earlybreak == False: 
            self.storage = ['']*4
            self.lastpos = 0
            self.prevmax = 0

        print("buf3=",buf[0:15])
        return i