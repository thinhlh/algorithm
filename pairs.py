# Right Solution


def pairs(k, arr) -> int:
    hash_map = {}
    res = 0
    # Write your code here

    for i in range(len(arr)):
        hash_map[arr[i]+k] = i

    for a in arr:
        if a in hash_map:
            res += 1

    return res


print(pairs(1, [1, 2, 3, 4]))
