from Week_05.practice.testing import TestCode
from typing import List


class Solution:
    """
    64. 最小路径和
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。

    示例:

    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp time_complexity: n
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        # l = len(grid)
        dp = [0] * len(grid[0])
        # for i in range(len(grid)):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    dp[j] = min(dp[j - 1] + grid[i][j], dp[j] + grid[i][j])
                elif i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif j == 0:
                    dp[j] = dp[0] + grid[i][j]
                else:
                    dp[j] = dp[j - 1] + grid[i][j]
                # print(dp)
        return dp[-1]


def main():
    test_case = [
                    ([
                      [1, 3, 1],
                      [1, 5, 1],
                      [4, 2, 1]
                        ],),
                    ([[1, 2], [1, 1]],),
                    ([
                         [1, 3, 1],
                         [1, 0, 1],
                         [4, 2, 1]
                     ],),
                    ([[]],), ([[1]],),

                    ]
    tester = TestCode()
    tester.creat_function(Solution().minPathSum)
    tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
