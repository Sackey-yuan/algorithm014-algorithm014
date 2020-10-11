class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.dfs([], 0, 0, n)
        return self.res
    
    def dfs(self, queens, xy_dif, xy_sum, n):
        row = len(queens)
        if row == n:
            self.res += 1
        for next_queens in range(n):
            if next_queens not in queens and  not (1 & (xy_dif >> (n +  row - next_queens))) and not (1 & (xy_sum >> ( row + next_queens))) :
                self.dfs(queens + [next_queens], xy_dif | (1 << (n + row - next_queens)), xy_sum | (1 << (row + next_queens)), n)