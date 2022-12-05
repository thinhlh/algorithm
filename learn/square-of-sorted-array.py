# Solved
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        left_idx, right_idx = 0, len(nums)-1
        res = [0] * len(nums)

        while left_idx <= right_idx:
            left, right = abs(nums[left_idx]), abs(nums[right_idx])
            if left > right:
                res[right_idx-left_idx] = left**2
                left_idx += 1
            else:
                res[right_idx-left_idx] = right**2
                right_idx -= 1

        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
