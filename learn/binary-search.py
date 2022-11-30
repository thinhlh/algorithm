# Solved

class Solution:
    def binary_search(self, nums: list[int], target: int, left: int, right: int):
        while left <= right:
            mid = right+left//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                return self.binary_search(nums, target, mid+1, right)
            else:
                return self.binary_search(nums, target, left, mid-1)

        return -1

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)
