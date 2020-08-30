from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #递归解决
        res = []
        def dfs(nums,ans,k):
            if k == 0:
                res.append(ans)
            else:
                if len(nums) >= k:
                    for i in range(len(nums)):
                        if i + 1 < len(nums):
                            nextnums = nums[i+1:]
                        else:
                            nextnums = []
                        dfs(nextnums,ans+[nums[i]],k-1)
        dfs([i for i in range(1,1+n)],[],k)
        return res