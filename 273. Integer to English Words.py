class Solution:
    def __init__(self):
        self.d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"}
          
    def numberToWords(self, num: int) -> str:
        if int(num) in self.d and len(str(num)) < 3: 
            return self.d[int(num)]
        elif int(num) in self.d and len(str(num)) == 3: 
            return self.d[int(str(num)[0])] + " " + "Hundred"
        
        stack = ["Billion","Million","Thousand",""]
        num = str(num)
        first = len(num) % 3 
        rest = len(num) // 3 
        segments = [] 
        if first!= 0:
            segments.append(num[:first])
        for i in range(rest):
            segments.append(num[first:first+3])
            first = first + 3 
        ans = ""
        print(segments)
        for section in segments[::-1]:
            a = stack.pop()
            opt = " "
            if int(section)!=0:
                ans = self.calcthree(section) + " " + a + " " +  ans 
        return ans.strip()
    
    def calcthree(self, num:str) -> str: 
        if num == "":
            return ''
        elif num[0] == '0':
            return self.calcthree(num[1::])

        if int(num) in self.d and len(num) < 3 and num!='00' and num!='0': 
            return self.d[int(num)]
        elif int(num) in self.d and len(num) == 3: 
            return self.d[int(num[0])] + " " + self.d[int(num)]
        
        elif len(num) == 3: 
            suffix = self.calcthree(num[1::])
            if suffix:
                suffix = " " + suffix 
            return self.d[int(num[0])] + " " + "Hundred" + suffix 
        elif len(num) == 2:
            return self.d[int(num[0] + '0')] + " "+ self.calcthree(num[1::])
        elif len(num) == 1: 
            return self.d[int(num)]
         