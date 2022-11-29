# Right Solution


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            else:
                hash_map[target-nums[i]] = i


print(Solution().twoSum([2, 7, 11, 15], 9))
