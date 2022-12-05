class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        match_target = {}

        for i in range(len(numbers)):
            if numbers[i] in match_target:
                return [match_target[numbers[i]] + 1, i + 1]
            else:
                match_target[target-numbers[i]] = i
            print(match_target)


print(Solution().twoSum([2, 7, 11, 15], 9))
