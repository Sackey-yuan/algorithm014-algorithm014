
from Week_05.practice.testing import TestCode


class Solution:
    """
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

    示例 1:

    输入: 1
    输出: true
    解释: 20 = 1
    示例 2:

    输入: 16
    输出: true
    解释: 24 = 16
    示例 3:

    输入: 218
    输出: false

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/power-of-two
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isPowerOfTwo(self, n: int) -> bool:
        #最低1位为零
        return bool(n and n & (n - 1) == 0)
        # # 位移
        # while  n and not (n & 1) :
        #     n >>= 1
        # return n == 1
        # # #bin count
        # # return n > 0 and bin(n).count("1") == 1


def main():
    test_case = [(i,) for i in range(2, 100, 23)
                    ]
    tester = TestCode()
    tester.creat_function(Solution().isPowerOfTwo)
    tester.creat_test_case(test_case)
    tester.start()
    # tester.del_log_cache()


if __name__ == "__main__":
    main()
