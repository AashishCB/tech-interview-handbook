class Solution:

    def __init__(self):
        pass

    @staticmethod
    def two_sum(nums, target):
        for index in range(0, len(nums)-1):
            key = target - nums[index]
            if key in nums[index+1:]:
                return [index, nums[index+1:].index(key) + index + 1]


print(Solution().two_sum([3, 2, 4], 6))
print(Solution().two_sum([3, 3], 6))
print(Solution().two_sum([2, 5, 5, 7], 10))
