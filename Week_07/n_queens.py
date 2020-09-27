from typing import List
from Week_05.practice.testing import TestCode


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

def main():
    test_case = [(i,) for i in range(0, 10, 2)]
    tester = TestCode()
    tester.creat_function(Solution().solveNQueens)
    tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
