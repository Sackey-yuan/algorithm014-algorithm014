class Solution:
    """
    200. 岛屿数量
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

    岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

    此外，你可以假设该网格的四条边均被水包围。



    示例 1:

    输入:
    [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
    ]
    输出: 1
    示例 2:

    输入:
    [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
    ]
    输出: 3
    解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid:
            l1 = len(grid)
            l2 = len(grid[0])
            if l2 == 0 or l1 == 0:
                return 0
            res = 0

            def dfs(x, y):
                grid[x][y] = "0"
                if x + 1 < l1:
                    if grid[x + 1][y] == "1":
                        dfs(x + 1, y)
                if x - 1 >= 0:
                    if grid[x - 1][y] == "1":
                        dfs(x - 1, y)
                if y + 1 < l2:
                    if grid[x][y + 1] == "1":
                        dfs(x, y + 1)
                if y - 1 >= 0:
                    if grid[x][y - 1] == "1":
                        dfs(x, y - 1)

            for i in range(l1):
                for j in range(l2):
                    if grid[i][j] == "1":
                        res += 1
                        dfs(i, j)
            return res
        return 0

