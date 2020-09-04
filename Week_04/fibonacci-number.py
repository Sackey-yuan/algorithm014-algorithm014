class Solution:
    def fib(self, N: int) -> int:
        #递归+缓存 time_complexity：o(n) space_complexity:o(1)
        hash_dict = {0:0,1:1}
        def dfs(n):
            if n not in hash_dict:
                n1 = dfs(n-1)
                n2 = dfs(n-2)
                hash_dict[n] = n1+n2
            return hash_dict[n]
        return dfs(N)
        # #递推 time_complexity：o(n) space_complexity:o(1)
        # f1,f2 = 0,1
        # for _ in range(N):
        #     f1, f2 = f2 , f1+f2
        # return f1