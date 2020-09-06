class Solution:
    """
    367. 有效的完全平方数
    给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
    说明：不要使用任何内置的库函数，如  sqrt。
    示例 1：
    输入：16
    输出：True
    示例 2：
    输入：14
    输出：False
    """
    def isPerfectSquare(self, num: int) -> bool:
        #牛顿逼近法 time_complexity:O(log n)
        if num < 2:
            return True
        x = num//2
        while pow(x,2) > num:
            x = (x + num // x) // 2
        return pow(x,2) == num
        # #二分查找 time_complexity:o(logn)
        # if num < 2:
        #     return True
        # left , right = 0 , num
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     # print(left, right , mid)
        #     x = mid * mid
        #     if x > num:
        #         right = mid - 1
        #     elif x < num:
        #         left = mid + 1
        #     else:
        #         return True
        # return False
