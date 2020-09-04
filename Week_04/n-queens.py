from typing import List
class Solution:
    """
    https://leetcode-cn.com/problems/n-queens/
    51. N皇后
    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    示例:

    输入: 4
    输出: [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    解释: 4 皇后问题存在两个不同的解法。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/n-queens
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        #copy + 优化  40 ms	13.8 MB 99.97%
        res = []
        def dfs(queens,xy_dif,xy_sum):
            p = len(queens)
            if p == n:
                #res.append(queens)
                res.append(["." * i + "Q" + "." * (n - i - 1) for i in queens])
            for q in range(n):
                if q not in queens and p + q not in xy_sum and n - p+q not in xy_dif:
                    dfs(queens+[q],xy_dif+[n-p+q],xy_sum + [p+q])
        dfs([],[],[])
        # return [ ["." * i +"Q" + "." * (n-i-1) for i in s ] for s in res]
        return res

    def solveNQueens2(self, n: int) -> List[List[str]]:
        #44 ms	13.9 MB
        h, c, j = [1] * n, [1] * n * 2, [1] * n * 2
        check = [["."] * n for _ in range(n)]
        res = []
        def dfs(level):
            if level < n:
                # print(h,c,j)
                # print(check)
                for i in range(n):
                    # print(level,i)
                    if h[i] and c[level + i] and j[n - level + i]:
                        check[level][i] = "Q"
                        h[i], c[level + i], j[n - level + i] = 0, 0, 0
                        dfs(level + 1)
                        check[level][i] = "."
                        h[i], c[level + i], j[n - level + i] = 1, 1, 1
            else:
                res.append(["".join(check[i]) for i in range(n)])

        dfs(0)
        return res

s= Solution()
print(s.solveNQueens(6))