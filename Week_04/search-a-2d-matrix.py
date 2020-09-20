from typing import List
from Week_05.practice.testing import TestCode
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if matrix and matrix[0]:
        #     row = bisect.bisect(matrix, [target])
        #     if row < len(matrix) and matrix[row][0] == target:
        #         return True
        #     row -= 1
        #     ind = bisect.bisect_left(matrix[row], target)
        #     return ind < len(matrix[row]) and matrix[row][ind] == target
        # return False

        if not matrix or len(matrix[0]) == 0:
            return False

        left, right, n = 0, len(matrix) * len(matrix[0]), len(matrix[0])
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid//n, mid % n)
            curNum = matrix[mid // n][mid % n]
            if curNum == target:
                return True
            elif curNum > target:
                right = mid
            else:
                left = mid + 1
        return False


class Solution2:
    """
    74. 搜索二维矩阵
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    输出: true
    示例 2:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    输出: false
    通过次数60,125提交次数154,941
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #使用库函数 bisect
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = bisect.bisect(matrix, [target])
        if i < len(matrix) and matrix[i][0] == target :
            return True
        row = i - 1
        j = bisect.bisect_left(matrix[row],target)
        return  j < len(matrix[0]) and matrix[row][j] == target
        # # 类似跳表查询 time_complexity:o(m + n) 44 ms	14.6 MB
        # m = len(matrix)
        # if m == 0:
        #     return False
        # n = len(matrix[0])
        # if matrix[0][0] > target or matrix[m-1][n-1] < target:
        #     return False
        # x , y = 0, n-1
        # while x < m and matrix[x][y] <= target:
        #     if matrix[x][y] == target: return True
        #     x += 1
        # while y >= 0 and matrix[x][y] >= target:
        #     if matrix[x][y] == target:
        #         return True
        #     y -= 1
        # return False

class Solution1:
    """
    74. 搜索二维矩阵
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    输出: true
    示例 2:

    输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    输出: false
    通过次数60,125提交次数154,941
    """
    n = None
    m = None
    matrix = None
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # #使用二分查找，单独写一个函数来获取mid值 time_complexity:o(log(n*m)) 36 ms	14.7 MB
        # if not matrix and len(matrix[0]) == 0:
        #     return False
        # m ,n = len(matrix), len(matrix[0])
        # self.n = n
        # self.matrix = matrix
        # left , right = 0 , m * n -1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if self.mn(mid) == target:
        #         return True
        #     elif self.mn(mid) < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        #     return self.mn(left) == target
        #看题解后优化
        if not matrix or len(matrix[0]) == 0:
            return False
        n = len(matrix[0])
        left, right = 0, len(matrix)*n
        while left <= right:
            mid = (left + right) // 2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def mn(self, num):
        if num == 0:
            return self.matrix[0][0]
        if num%self.n:
            x = num//self.n
            y = num%self.n - 1
        else:
            x = num // self.n - 1
            y = self.n - 1
        return self.matrix[x][y]


if __name__ == "__main__":
    caseList = [([[1, 3, 5, 7],
                  [10, 13, 15, 20],
                  [23, 30, 34, 50]]
                , 13),
                ([[1, 3, 5, 7],
                  [10, 11, 16, 20],
                  [23, 30, 34,50]],
                 3),
                ([[]], 1),
                ([
                  [1,   3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 50]
                    ], 4),
                ([[i for i in range(k, k+100)] for k in range(0, 100000, 100)], 9999),
                ]
    caseList.extend([([[i for i in range(k, k+100)] for k in range(0,100000,100)], tar) for tar in range(33, 100000, 1000)])
    s = Solution()
    print(s.searchMatrix(caseList[0][0], caseList[0][1]))
    tester = TestCode()
    tester.creat_test_case(caseList)
    tester.creat_function(s.searchMatrix)
    # tester.start()
    tester.del_log_cache()