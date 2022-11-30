# Solved
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = {}
        for a in arr:
            if a in occurrences:
                occurrences[a] += 1
            else:
                occurrences[a] = 1
        print(occurrences)

        # The unique number in arr equals to the number of key-value pair in occurrence
        # If then we distinct the values (have same occurences) then if 2 keys have same occurence will be removed
        # Hence the len will not equal

        return len(set(arr)) == len(set(occurrences.values()))


print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
