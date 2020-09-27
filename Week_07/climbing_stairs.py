from functools import lru_cache
from Week_05.practice.testing import TestCode


class Solution:
    def dynamic(self, n):
        dp = [0, 1]
        for i in range(n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[0]

    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


def main():
    test_case = [(2,), (3,), (4,), (5,),
                    ]
    tester = TestCode()
    tester.creat_function(Solution().dynamic)
    tester.creat_test_case(test_case)
    tester.start()
    # tester.del_log_cache()


if __name__ == "__main__":
    main()
