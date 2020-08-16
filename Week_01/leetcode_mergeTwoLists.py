class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #递归 + 缓存 time_complexity:o(n),space_complexity:o(n)
        
        hash_map = {}
        def help(nums_list):
            if len(nums_list) == 0:
                return []
            i , val = nums_list.pop()
            if target - val in hash_map:
                return [i,hash_map[target - val]]
            else:
                hash_map[val] = i
                return help(nums_list)
        num_list = list(enumerate(nums))
        return help(num_list)

        
        # #hashmap time_complexity:o(n) space_complexity:o(n)
        # hash_map = {}
        # for i in range(len(nums)):
        #     if nums[i] in hash_map.keys():
        #         return [hash_map[nums[i]],i]
        #     else:
        #         diff = target - nums[i]
        #         hash_map[diff] = i

        # return []   