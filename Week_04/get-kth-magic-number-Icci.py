class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        #使用for替换while循环
        ans = [1]
        n, n3, n5, n7 = 0, 0, 0, 0
        r3, r5, r7 = ans[n3] * 3, ans[n5] * 5, ans[n7] * 7
        for i in range(k - 1):
            # while True:
            # n +=1
            # if n == k: return ans[-1]
            # r3, r5, r7 = ans[n3] * 3, ans[n5] * 5, ans[n7] * 7
            minN = min(r3, r5, r7)
            ans.append(minN)
            # print(n, minN, ans)
            if n == k: return minN
            if minN == r3:
                n3 += 1
                r3 = ans[n3] * 3
            if minN == r5:
                n5 += 1
                r5 = ans[n5] * 5
            if minN == r7:
                n7 += 1
                r7 = ans[n7] * 7
        return ans[-1]
        #
        #
        # ans = [1]
        # n, n3, n5, n7 = 0, 0, 0, 0
        # while True:
        #     n += 1
        #     if n == k: return ans[-1]
        #     r3, r5, r7 = ans[n3] * 3, ans[n5] * 5, ans[n7] * 7
        #     minN = min(r3, r5, r7)
        #     ans.append(minN)
        #     # n += 1
        #     print(n, minN, ans)
        #     if n == k: return minN
        #     if minN == r3: n3 += 1
        #     if minN == r5: n5 += 1
        #     if minN == r7: n7 += 1
        #
        #
        #
        #     # ans = []
        #     # for i in range(k):
        #     #     for j in range(k):
        #     #         for z in range(k):
        #     #             ans.append((3**i)*(5**j)*(7**z))
        #     # # print(ans)
        #     # ans.sort()
        #     # # print(ans)
        #     # return ans[k-1]