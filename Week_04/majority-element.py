from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 使用库函数counter 48 ms	14.9 MB
        c = Counter(nums)
        l = len(nums)
        for i in c:
            if c[i] >= l/2:
                return i
        # #使用库函数list。sort（）time_complexity:o(log n) 48 ms	15.2 MB
        # nums.sort()
        # return nums[len(nums)//2]
        # ##time_complexity:o(n) space_complexity:o(n)88 ms	15 MB
        # # hash_map = {}
        # # l, n =0, len(nums)
        # # for i in range(n):
        # #     l = hash_map.get(nums[i],0) + 1
        # #     if l > n/2:
        # #         return nums[i]
        # #     hash_map[nums[i]] = l
        # # return None
ask = [1,2,2,2]
s = Solution()
print(s.majorityElement(ask))
