from typing import List
from Week_05.practice.testing import TestCode
class Solution:
    """
    77. 组合
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

    示例:

    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1,n+1),k))
        # res = []
        # def dfs(cur,kk,nums):
        #     if kk == k:
        #         res.append(nums)
        #     else:
        #         for i in range(cur,n-k+kk+2):
        #             dfs(i+1,kk+1,nums+[i])
        # dfs(1,0,[])
        # # print(res)
        # return res
if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))
    t = TestCode()
    t.del_log_cache()