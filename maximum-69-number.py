class Solution:
    def maximum69Number(self, num: int) -> int:
        result = []
        while num != 0:
            digit = num % 10
            result.insert(0, digit)
            num //= 10

        num = 0
        changed = False
        print(result)
        for i in range(len(result)):
            if (changed == False and result[i] == 6):
                changed = True
                result[i] = 9
            num += result[i] * 10 ** (len(result) - 1 - i)

        return num


print(Solution().maximum69Number(int(input())))
