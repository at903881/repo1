def numIslands(grid):

    def fun(grid, i, j):
        nonlocal vis
        if grid[i][j] == '0':
            return
        if vis[i][j]:
            return
        m = len(grid)
        n = len(grid[0])

        vis[i][j] = 1
        if i - 1 >= 0:
            fun(grid, i - 1, j)
        if j - 1 >= 0:
            fun(grid, i, j - 1)
        if i + 1 < m:
            fun(grid, i + 1, j)
        if j + 1 < n:
            fun(grid, i, j + 1)

    m = len(grid)
    n = len(grid[0])
    ans = 0
    vis = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if vis[i][j] == 0 and grid[i][j] == '1':
                ans += 1
                fun(grid, i, j)
    for v in vis:
        print(v)
    return ans

print(numIslands([["1","0","1"],["0","1","0"],["1","0","1"]]))