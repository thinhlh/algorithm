# There are 3 cases
# First we need to split into [negatives number list] and [positive number list]
# [0,0,0] Only exist if number of zeros >=3 | Add to result once if numbers of zero >=3
# [-,0,+] 2 oposite numbers | Find if is there any number in positive equal to (-1*number in negative) then add once
# [-,-,+] 2 negative and 1 positive | Find the total 2 negative number exists in positive list
# [+,+,-] 2 postivie and 1 negative | Find the toal 2 positive numbers exists in negative list


class Solution(object):
    def threeSum(self, nums):
        positives = []
        negatives = []
        zeros = 0
        output = set()
        nums.sort()
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros = zeros+1

        P, N = set(positives), set(negatives)

# I Have tried it without Set, but it just exceed Time limit I put explanation in Above feel free to read

        PosTotal = len(positives)
        negTotal = len(negatives)

        # Case 4
        for a in range(PosTotal):
            for b in range(a+1, PosTotal):
                Target = (positives[a]+positives[b])*(-1)
                if Target in N:
                    output.add(
                        tuple(sorted((positives[a], positives[b], Target))))

        # Case 3
        for a in range(negTotal):
            for b in range(a+1, negTotal):
                target = (negatives[a]+negatives[b])*-1
                if target in P:
                    output.add(
                        tuple(sorted((target, negatives[a], negatives[b]))))

        # Case 2
        if zeros != 0:
            for p in positives:
                if -p in N:
                    output.add((p, -p, 0))

        # Case 1
        if zeros > 2:
            output.add((0, 0, 0))

        return output
