
from Week_05.practice.testing import TestCode


class Solution:
    def reverseBits(self, n: int) -> int:
        # #bin zfill
        return int( bin(n)[2::].zfill(32)[::-1], base=2)
        # # # 位移
        # # res = 0
        # # for i in range(32):
        # #     res = (res << 1) + (n & 1)
        # #     n >>= 1
        # # return res


def main():
    test_case = [(i,) for i in range(0, 299, 56)
                    ]
    tester = TestCode()
    tester.creat_function(Solution().hammingWeight)
    tester.creat_test_case(test_case)
    # tester.start()
    # tester.del_log_cache()


if __name__ == "__main__":
    main()
