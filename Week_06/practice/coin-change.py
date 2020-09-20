import functools
from typing import List
from Week_05.practice.testing import TestCode


class Solution:
    """
    322. 零钱兑换
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，
    返回 -1。



    示例 1:

    输入: coins = [1, 2, 5], amount = 11
    输出: 3
    解释: 11 = 5 + 5 + 1
    示例 2:

    输入: coins = [2], amount = 3
    输出: -1
    """
    def coin_change(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def recursion(n):
            if n < 0:
                return float("inf")
            if n == 0:
                return 0
            mini = float("inf")
            for i in coins:
                mini = min(mini, recursion(n - i) + 1)
            return mini
        return recursion(amount) if recursion(amount) != float("inf") else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp function time_complexity: o(len(coins)*amount)
        dp = [0] + [int(1e9)] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != int(1e9) else -1


if __name__ == "__main__":
    testcase = [([1, 2, 5], 11,), ([1, 2, 5], 200,), ([2], 3)]
    tester = TestCode()
    tester.creat_test_case(testcase)
    s = Solution()
    tester.creat_function(s.coinChange)
    tester.start()
