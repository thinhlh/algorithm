class Solution:
    def climbStairs(self, n: int) -> int:
        moves = [1] * (n)
        i = 1
        while i < n:
            moves[i] = moves[i-1] + moves[i-2]
            i += 1
        return moves[-1]


print(Solution().climbStairs(2))
