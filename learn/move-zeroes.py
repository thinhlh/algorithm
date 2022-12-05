class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        i = 0
        while True:
            if i < len(nums):
                if nums[i] == 0:
                    zeros += 1
                    nums.pop(i)
                else:
                    i += 1
            else:
                break
        nums += ([0]*zeros)


nums = [0, 1, 0, 3, 12]
nums = [0, 0, 1]
Solution().moveZeroes(nums)
print(nums)
