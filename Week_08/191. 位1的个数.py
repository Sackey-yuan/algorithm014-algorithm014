
from Week_05.practice.testing import TestCode


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 位运算 最低位1置换为零
        print(bin(n))
        res = 0 # 1 if n else 0
        # while n := n & (n - 1): #Python 3.8 code == 10 + 11
        while n:
            n = n & (n - 1)
            res += 1
        return res
        # # 位移
        # res = 0
        # while n :
        #     res += n & 1
        #     n >>= 1
        # return res

        # # # 库函数 bin + count 44 ms	13.3 MB
        # # return bin(n).count("1")


def main():
    test_case = [(i,) for i in range(0, 299, 56)
                    ]
    tester = TestCode()
    tester.creat_function(Solution().hammingWeight)
    tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()
