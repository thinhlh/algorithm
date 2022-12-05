# Solved

def gridChallenge(grid: list[str]):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = ''.join(list(sorted(list(grid[i]))))
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if grid[j][i] > grid[j+1][i]:
                return False

    return True


print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
