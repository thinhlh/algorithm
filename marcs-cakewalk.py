# Right Solution

import math


def marcsCakewalk(calorie):
    # Write your code here
    calorie = sorted(calorie, reverse=True)
    total = 0

    for i in range(len(calorie)):
        total += int(math.pow(2, i)) * calorie[i]
    return total


print(marcsCakewalk([1, 3, 2]))
