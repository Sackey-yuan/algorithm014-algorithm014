class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        visited, res = [], 0
        for num in nums[::-1]:
            res += bisect.bisect_left(visited, num)
            loc = bisect.bisect_left(visited, num  * 2)
            visited[loc:loc] = [num * 2] # 1632 ms	20.2 MB
            # bisect.insort(visited, num * 2) # 2592 ms	20.3 MB
        return res
        # if len(nums) < 2:
        #     return 0
        # visited, res = [], 0
        # for i in range(len(nums)-1, -1, -1):
        #     res += bisect.bisect_left(visited, nums[i])
        #     bisect.insort_left(visited, nums[i] * 2) # 使用bisect.insort_left优化
        #     # print(nums[i], visited, ind)
        #     # # visited.insert(bisect.bisect_right(visited, 2 * nums[i]), 2 * nums[i]) # 简化
        #     # loc = bisect.bisect_right(visited, 2 * nums[i])
        #     # visited[loc:loc] = [nums[i] * 2] # 新学习到的插入list中的方法
        # return res