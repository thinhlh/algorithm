from collections import Counter


class Solution:
    def removeDuplicatesII(self, nums: list[int]) -> int:
        i = 1
        item_duplicated_once = False
        while i < len(nums):
            print(i, item_duplicated_once, nums)
            if nums[i] == nums[i-1]:
                if item_duplicated_once:
                    nums.pop(i)
                else:
                    item_duplicated_once = True
                    i += 1
            else:
                item_duplicated_once = False
                i += 1

        return len(nums)


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicatesII(nums))
print(nums)
