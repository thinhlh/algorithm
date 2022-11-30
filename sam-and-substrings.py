# NOT FINISHED

def substrings(n):
    # res = [0] * ((n*(n+1))//2)
    res = []
    for i in range(len(n)):
        for j in range(0, i+1):
            res.append(int(n[j:i+1]))

    return int(sum(res) % (10e8+7))
    pass


print(substrings('972698438521'))
