# Solved
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return list(sorted([num**2 for num in nums]))


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
