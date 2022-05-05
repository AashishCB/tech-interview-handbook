class Solution:

    @staticmethod
    def contains_duplicate(nums):
        return "false" if len(set(nums)) == len(nums) else "true"


print(Solution().contains_duplicate([1, 2, 3, 1]))
print(Solution().contains_duplicate([1, 2, 3, 4]))
print(Solution().contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(Solution().contains_duplicate([11, 1000000000, 100000000, 12]))
