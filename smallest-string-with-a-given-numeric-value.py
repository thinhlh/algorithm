class Solution:
    def get_value_from_char(self, char: str) -> int:
        return ord(char) - 96

    def get_char_from_value(self, value: int) -> str:
        return chr(value + 96)

    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        if k > self.get_value_from_char('z'):
            return ''
        else:
            return self.get_char_from_value(k)


print(Solution().getSmallestString(3, 26))
