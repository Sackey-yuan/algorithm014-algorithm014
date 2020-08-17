from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # #暴力 使用函数min（） 36 ms	13.8 MB
        # return min(numbers)

        # #二分查找 time_complexity O（log n）-> o(n) 44 ms	13.7 MB
        # low , hight = 0 , len(numbers) - 1
        # if numbers[low] < numbers[hight]:
        #     return numbers[low]
        # while low < hight:
        #     pivot = ( hight + low) // 2
        #     if numbers[pivot] > numbers[hight]:
        #         low = pivot + 1
        #     elif numbers[pivot] < numbers[hight]:
        #         hight = pivot 
        #     else:
        #         hight -= 1
        # return numbers[low]


        # # #递归 O(n) 224 ms	78.8 MB
        # # def help(a , numbers):
        # #     if numbers:
        # #         #print(a,numbers,numbers[0])
        # #         if a > numbers[0]:
        # #             return numbers[0]
        # #         else:
        # #             return help(numbers[0],numbers[1:])
        # #     else:
        # #         return None
        # # res = help(numbers[0],numbers[1:])
        # # if res is None:
        # #     return numbers[0]
        # # return res

        #指针遍历 o(n) 44 ms	14 MB
        for i in range(len(numbers) - 1):
            # if i > 0:
            #     if numbers[i] < numbers[i-1]:
            #         return numbers[i]
            if numbers[i] > numbers[i+1]:
                return numbers[i + 1]
        return numbers[0]