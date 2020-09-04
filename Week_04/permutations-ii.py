from typing import List
class Solution:
    """
    给定一个可包含重复数字的序列，返回所有不重复的全排列。

    示例:

    输入: [1,1,2]
    输出:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    链接：https://leetcode-cn.com/problems/permutations-ii
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        nums.sort()
        def dfs(n,ans, nums):
            if n == l:
                res.append(ans)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                dfs(n+1,ans+[nums[i]],nums[0:i]+nums[i+1:])
        dfs(0,[],nums)
        return res

ns = [1,2,3,3]
s = Solution()
print(s.permuteUnique(ns))


