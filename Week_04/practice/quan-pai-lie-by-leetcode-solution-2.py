# from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums):
        #库函数
        return list(permutations(nums))

class Solution2:
    def permute(self, nums):
        #dfs time_complexity:o(n!) space_complexity:O(n!)
        res = []
        def dfs(numlist,ans):
            # print(numlist,ans,res)
            l = len(numlist)
            if l > 0:
                for i in range(len(numlist)):
                    # remain = numlist[0:i] if i + 1 == l else numlist[0:i] + numlist[i + 1:]
                    remain = numlist[0:i] + numlist[i+1:]
                    dfs(remain,ans+[numlist[i]])
            else:
                res.append(ans)
        dfs(nums,[])
        return res
    def oneLine(self,nums):
        return[[n] + p
                        for i, n in enumerate(nums)
                        for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

nums = [1,2,3]
s = Solution2()
print(s.oneLine(nums))