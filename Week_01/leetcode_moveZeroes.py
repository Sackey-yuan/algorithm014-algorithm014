class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #双指针+ 交换操作 time_complexity：o（n） space_complexity：o（1）44 ms	14.3 MB
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                if i != non_zero:
                    nums[i] , nums[non_zero] = nums[non_zero] , nums[i]
                non_zero += 1
        return nums

        # #双指针+两次遍历 time_complexity：O（2n），space_complexity：o（1） 44 ms	14.4 MB
        # non_zero = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0 :
        #         if i > non_zero:
        #             nums[non_zero] = nums[i]
        #         non_zero += 1
        # for i in range(non_zero,len(nums)):
        #     nums[i] = 0
        # return nums