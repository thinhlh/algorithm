# Solved
class Solution:
    def isBadVersion(self, version: int) -> bool:
        return version >= 7

    def findFirstBadVersionInRange(self, left: int, right: int) -> int:
        if left >= right:
            return left
        mid = (right+left)//2
        # print(left, mid, right, self.isBadVersion(mid))
        if self.isBadVersion(mid):
            # Already bad
            return self.findFirstBadVersionInRange(left, mid)
        else:
            # Not yet bad
            return self.findFirstBadVersionInRange(mid+1, right)

    def firstBadVersion(self, n: int) -> int:
        return self.findFirstBadVersionInRange(1, n)


print(Solution().firstBadVersion(10))
