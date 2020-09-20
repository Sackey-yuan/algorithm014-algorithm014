from typing import  List
from Week_05.practice.testing import TestCode


class Solution:
    """
    221. 最大正方形
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

    示例:

    输入:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    输出: 4
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows, columns = len(matrix), len(matrix[0])
        print(rows, columns)
        dp = [[0] * columns for i in range(rows)]
        max_row = 0
        # for i in range(len(matrix)):
        #     dp[i][0] = 1 if matrix[i][0] == "1" else 0
        #     max_row = dp[i][0] if dp[i][0] > max_row else max_row
        # for i in range(len(matrix[0])):
        #     dp[0][i] = 1 if matrix[0][i] == "1" else 0
        #     max_row = dp[0][i] if dp[0][i] > max_row else max_row
        for i in range(rows):
            for j in range(columns):
                # print("asa0", i, j, matrix[i][j])
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        # print("asa1", i, j)
                        dp[i][j] = 1
                    else:
                        # print("asa2", i, j)
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                max_row = dp[i][j] if dp[i][j] > max_row else max_row
        # print(dp)
        return max_row ** 2


def main():
    test_case = [([["1","0","1","0","0"],
                   ["1","0","1","1","1"],
                   ["1","1","1","1","1"],
                   ["1","0","0","1","0"]],), ([[]],), ([["1"]],), ([["0"]],)
                    ]
    """[[1, 0, 1, 0, 0], 
        [1, 0, 1, 1, 1], 
        [1, 1, 1, 2, 2], 
        [1, 0, 0, 1, 0]]
    """
    tester = TestCode()
    tester.creat_function(Solution().maximalSquare)
    tester.creat_test_case(test_case)
    tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
