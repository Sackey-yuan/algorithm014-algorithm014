from typing import List
from Week_05.practice.testing import TestCode

class Solution:
    """
    560. 和为K的子数组
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

    示例 1 :

    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :

    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        res, per, n = 0, {0: 1}, len(nums)
        nSum = 0
        for i in range(n):
            nSum += nums[i]
            res += per.get(nSum - k, 0)
            per[nSum] = per.get(nSum, 0) + 1
        return res


if __name__ == "__main__":
    caseList = [([1, 1, 1] * 10000, 2)]
    testCode = TestCode()
    testCode.creat_test_case(caseList)
    s = Solution()
    testCode.creat_function(s.subarraySum)
    testCode.start()