
# Solved

import math


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        tabulation = [-10e4] + [0] * len(nums)

        for i in range(1, len(nums)+1):
            tabulation[i] = max(tabulation[i-1] + nums[i-1], nums[i-1])
        return max(tabulation)


print(Solution().maxSubArray([-1]))
