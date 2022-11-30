class Solution:
    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        mid = (left + right)//2
        if left > right:
            return left
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binary_search(nums, target, left, mid-1)
        else:
            return self.binary_search(nums, target, mid+1, right)

        pass

    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)


print(Solution().searchInsert([1, 3, 5, 6], 7))
