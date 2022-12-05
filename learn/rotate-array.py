class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Solution 1
        # for i in range(k):
        #     nums.insert(0, nums.pop(len(nums)-1))

        # Solution 2
        # We will break the array to 2 parts, first array has length n-k, second array will have k elemenets
        # [1, 2, 3, 4, 5, 6, 7], k=3 => [1,2,3,4] => [5,6,7]

        # Merge 2 array with array 2 before array 1
        # If k % n == 0 => Our nums is remain the same, then we have to module by k
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, k=3)
print(nums)
