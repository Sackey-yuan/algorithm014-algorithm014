from typing import List
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 优化
        if len(nums) < 2:
            return 0
        visited, res = [], 0
        visited.append(nums[-1] * 2)
        for i in range(len(nums) - 2, -1, -1):
            res += bisect.bisect_left(visited, nums[i])
            bisect.insort_left(visited, nums[i] * 2)
            # loc = bisect.bisect_right(visited, 2 * nums[i])
            # visited[loc:loc] = [nums[i] * 2]
            # # visited.insert(bisect.bisect_right(visited, 2 * nums[i]), 2 * nums[i])
        return res


        # if len(nums) < 2:
        #     return 0
        # visited, res = [], 0
        # visited.append(nums[-1] * 2)
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] > visited[0]:
        #         ind = bisect.bisect_left(visited, nums[i])
        #         res += ind
        #         # print(nums[i], visited, ind)
        #     visited.insert(bisect.bisect_right(visited, 2 * nums[i]), 2 * nums[i])
        # return res
