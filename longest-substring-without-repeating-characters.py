class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            current = []
            current.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in current:
                    current.append(s[j])
                else:
                    break
            res = max(res, len(current))
        return res


print(Solution().lengthOfLongestSubstring(' '))
