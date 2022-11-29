# NOT YET SUCCEED

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    # Write your code here
    arr: list[int] = []
    cost = 0
    for row in s:
        arr += row

    duplicated = []
    mark_missing_value_before_duplicated = False
    arr.sort()
    for i in range(1, len(arr)+1):
        if i == len(arr):
            if len(duplicated) != 0:
                cost += (arr[i-1]+1-duplicated.pop(0))
            break
        # 112 with 1 is duplicated
        if arr[i-1] == arr[i]:
            if mark_missing_value_before_duplicated:
                duplicate_value = duplicated.pop(0)
                cost += arr[i] - duplicate_value
                mark_missing_value_before_duplicated = False
            else:
                duplicated.append(arr[i])
        elif arr[i-1] + 1 == arr[i]:
            # Normal behavior
            pass
        else:
            # 13 with 3>1+1
            # arr[i] > arr[i-1] +1
            if len(duplicated) == 0:
                duplicated.append(arr[i-1]+1)
                mark_missing_value_before_duplicated = True
            else:
                duplicate_value = duplicated.pop(0)
                cost += (arr[i-1] + 1 - duplicate_value)

    return cost


result = formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
print(result)
