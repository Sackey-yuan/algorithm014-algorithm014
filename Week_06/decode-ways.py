from Week_05.practice.testing import TestCode


class Solution:
    """
    91. 解码方法
    一条包含字母 A-Z 的消息通过以下方式进行了编码：

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。

    示例 1:

    输入: "12"
    输出: 2
    解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
    示例 2:

    输入: "226"
    输出: 3
    解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
    """
    def numDecodings(self, s: str) -> int:
        # dp complexity:O(n)
        if len(s) == 0 or s[0] == "0":
            return 0
        dp = [1, 1] + [0] * len(s)
        dp = dp[:-1]
        for i in range(1, len(s)):
            if '1' <= s[i] <= '9':
                dp[i + 1] += dp[i]
            if '10' <= s[i-1: i+1] <= '26':
                dp[i + 1] += dp[i-1]
        return dp[-1]


    def numDecodings1(self, s: str) -> int:
        # dp 优化 time_complexity: o(n)
        if len(s) == 0 or s[0] == "0":
            return 0
        per2, per1 = 1, 1
        for i in range(1, len(s)):
            print(s[i], s[i-1:i+1])
            cur = 0
            if '1' <= s[i] <= '9':
                cur += per1
            #     dp[i] += dp[i - 1]
            #     # print(dp)
            if '10' < s[i-1:i+1] <= "26":
                cur += per2
            per2, per1 = per1, cur
            #     dp[i] += dp[i - 2]
            #     # print(dp)
            # #     if i == 0:
            # #         dp[i] = 1
            # #     elif dp[i-1] == '1' or (s[i] in '123456' and s[i-1] in '12'):
            # #         dp[i] = dp[i-1] + dp[i - 2]
            # #     dp[i] += dp[i-1]
            # # else:
            # #     if i == 0 or s[i-1] not in '12':
            # #         return 0
            # #     else:
            # #         dp[i] = dp[i-1]
            # #
            # #     dp[i] = dp[i-1]
        return per1


def main():
    test_case = [("123",), ("12",), ("1",), ("0",), ("10",), ("19",), ("21",), ("27",), ("271",), ("2",), ("1203",), ("12003",), ("121345143",)]
    tester = TestCode()
    tester.creat_function(Solution().numDecodings)
    tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
