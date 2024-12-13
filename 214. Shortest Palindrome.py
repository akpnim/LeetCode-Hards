#You are given a string s. You can convert s to a palindrome 
#by adding characters in front of it. Return the shortest palindrome you can find by performing this transformation.
#Can be improved by using K-M-P alogirthm! 

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s 
        possible_pivots = [i for i in range(len(s)//2)][::-1]
        print(possible_pivots)
        for pivot in possible_pivots:
            if s[pivot:pivot+2] == s[pivot:pivot+2][::-1]: #basically if there is a dual pivot 
                if s[:pivot] == s[pivot+2:pivot+2+len(s[:pivot])][::-1]:
                    return s[pivot+2+len(s[:pivot])::][::-1] + s

            if s[:pivot] == s[pivot+1:pivot+1+len(s[:pivot])][::-1]:
                return s[pivot+1+len(s[:pivot])::][::-1] + s 

test = Solution()
s = "abcd"
print(test.shortestPalindrome(s))