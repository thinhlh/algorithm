# Right Solution


class Solution:

    def binary_search(self, nums, target, left, right, find_max_left) -> int:

        if (right >= left):
            mid = (left + right)//2

            if (target == nums[mid]):
                if find_max_left:
                    res = self.binary_search(nums, target, left,
                                             mid-1, find_max_left)
                    if (res == -1):
                        return mid
                    else:
                        return res
                else:
                    res = self.binary_search(nums, target, mid+1, right,
                                             find_max_left)
                    if (res == -1):
                        return mid
                    else:
                        return res
            if (target > nums[mid]):
                return self.binary_search(nums, target, mid+1, right, find_max_left)
            if (target < nums[mid]):
                return self.binary_search(nums, target, left, mid-1, find_max_left)
        else:
            return -1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if self.binary_search(nums, target, 0, len(nums)-1, True) == -1:
            return [-1, -1]
        else:
            left = self.binary_search(nums, target, 0, len(nums)-1, True)
            right = self.binary_search(nums, target, 0, len(nums)-1, False)

            return [left, right]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

# l = 0
# r = 5
# m = 2
# == =
# l = 3
# r = 5
# m = 4

# == = > 4

# = Left
# l = l-1
# r = m-1
# = Right
