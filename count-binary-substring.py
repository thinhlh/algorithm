class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            zero, one = 0, 0
            if s[i] == '0':
                # Count consevacutive 0
                while (i < len(s) and s[i] == '0'):
                    i += 1
                    zero += 1

                # Store the
                j = i
                while (j < len(s) and s[j] == '1'):
                    j += 1
                    one += 1
            else:  # s[i] =='1'
                while (i < len(s) and s[i] == '1'):
                    i += 1
                    one += 1
                j = i
                while (j < len(s) and s[j] == '0'):
                    j += 1
                    zero += 1

            res += min(zero, one)
            print(zero, one, res)
            # e.g '0011', there are 2 zeros, 2 ones => Maximum 2 substring 0011 and 01
            # e.g '00011', there are 3 zeros, 2 ones => Only maximum 2 substring 0011 and 01, the exclude zero does not count
            # The number of substring in an consevacutive is min(zeros,ones)

        return res


print(Solution().countBinarySubstrings('00110011'))
