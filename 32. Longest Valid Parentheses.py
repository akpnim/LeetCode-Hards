class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = []
        for char in s:
            if char == '(':
                stack.append(char)
            if char == ')':
                if stack: 
                    ind = ''.join(stack).rfind('(')
                    if ind!= -1: 
                        stack[ind] = '1'
                    else: 
                        ind2 = ''.join(stack).find('1')
                        if ind2 != -1: 
                            ans.append(''.join(stack[ind2::]))
                            stack = []
        stack_ans = ''.join(stack).split('(')
        lengths_one = [len(i) for i in stack_ans]
        lengths_two = [len(i) for i in ans]
        lengths = lengths_one + lengths_two

        #print(stack_ans,ans, max(lengths))
        return max(lengths)*2

                        

        
test = Solution()
s = ")(((((()())()()))()(()))("

print(test.longestValidParentheses(s))