
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        dict_nums = {i for i in range(1,len(nums)+2)}
        for element in nums:
            if element in dict_nums:
                dict_nums.remove(element)
        return min(dict_nums)

test = Solution()
test1 = [1,2,0]
test2 = [3,4,-1,1]
test3 = [7,8,9,11,12]

print(test.firstMissingPositive(test1))
print(test.firstMissingPositive(test2))
print(test.firstMissingPositive(test3))
