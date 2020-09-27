from typing import List
from Week_05.practice.testing import TestCode


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # SET() DP time_complexity: O(n) space_complexity:o(1) TESTCASE ([(i,) for i in range(1, 20, 11)] ) timeSum:1109.063387ms
        dp = set(['()'])
        for i in range(1, n):
            dp = set(per[0:j] + "()" + per[j:] for per in dp for j in range(2 * i))
        return list(dp)


    def generate_yield(self, n) -> List[str]:
        # 生成器写法 # SET() DP time_complexity: O(n) space_complexity:o(1) TESTCASE ([(i,) for i in range(1, 20, 11)] ) timeSum:822.046995ms
        def help_func(s, left, right):
            if not right:
                yield s
            if left > 0:
                for x in help_func(s + "(", left - 1, right):
                    yield x
            if right > left:
                for y in help_func(s + ")", left, right - 1):
                    yield y
        return list(help_func('', n, n))

def main():
    test_case = [(i,) for i in range(1, 20, 11)]
    tester = TestCode()
    tester.creat_function(Solution().generate_yield)
    tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
