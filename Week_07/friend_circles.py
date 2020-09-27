from typing import List
from Week_05.practice.testing import TestCode


class SolutionUnion:
    parent = []

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        if n < 1:
            return 0
        self.parent = [-1 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    self.union(i, j)
        return self.parent.count(-1)

    def union(self, i, j):
        parent1 = self.find(i)
        parent2 = self.find(j)
        if parent1 != parent2:
            self.parent[parent1] = parent2

    def find(self, i):
        if self.parent[i] == -1:
            return i
        parents = self.find(self.parent[i])
        if self.parent[i] != parents:
            self.parent[i] = parents
        return parents


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        p = {i: {i} for i in range(n)}  # 并查集初始化
        ans = n
        # print(M)
        for i in range(n):
            for j in range(i, n):  # 遍历邻接矩阵
                if M[i][j] == 1 and p[i] is not p[j]:
                    p[i] |= p[j]  # 集合合并
                    for k in p[j]:  # 改变被合并的集合内元素指向
                        # print(i, j, k)
                        p[k] = p[i]
                    ans -= 1  # 减少朋友圈
            # print(p)
        return ans


def main():
    test_case = [([[1, 1, 0], [1, 1, 0], [0, 0, 1]],),
                 ([[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1],
                   [0, 0, 1, 1, 0],
                   [0, 0, 1, 0, 1],
                   ],),
                 ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   ],)
                 ]
    tester = TestCode()
    tester.creat_function(Solution().findCircleNum)
    tester.creat_test_case(test_case)
    tester.start()
    # tester.del_log_cache()


if __name__ == "__main__":
    main()
