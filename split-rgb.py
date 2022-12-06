# Solved
# Have an rgb color with red = 0, green = 1, blue = 2
# [2,1,0,2,0,2,1,0,1] => Using with On time complexity, group these color to an array => [0,0,0,1,1,1,2,2,2]

from collections import Counter


def group_color(colors: list[int]):
    res = []
    for key, value in Counter(colors).items():
        res += [key]*value
    return res


print(group_color([2, 1, 0, 2, 0, 2, 1, 0, 1]))
