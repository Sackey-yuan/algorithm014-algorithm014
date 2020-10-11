class Solution1:
    """位运算"""
    res = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.dfs([], 0, 0, n)
        return self.res
    
    def dfs(self, queens, xy_dif, xy_sum, n):
        row = len(queens)
        if row == n:
            self.res.append(['.' * i + "Q" + "." * (n - 1 - i) for i in queens])
        for next_queens in range(n):
            if next_queens not in queens and  not (1 & (xy_dif >> (n +  row - next_queens))) and not (1 & (xy_sum >> ( row + next_queens))) :
                self.dfs(queens + [next_queens], xy_dif | (1 << (n + row - next_queens)), xy_sum | (1 << (row + next_queens)), n)


class Solution:
    res = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.dfs([], [], [], n)
        return self.res
    
    def dfs(self, queens, xy_dif, xy_sum, n):
        row = len(queens)
        if row == n:
            self.res.append(['.' * i + "Q" + "." * (n - 1 - i) for i in queens])
        for next_queens in range(n):
            if next_queens not in queens and (row - next_queens) not in xy_dif and (row + next_queens) not in xy_sum:
                self.dfs(queens + [next_queens], xy_dif + [row - next_queens], xy_sum + [row + next_queens], n)