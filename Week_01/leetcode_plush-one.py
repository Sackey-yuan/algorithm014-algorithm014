class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #尾指针 + 缓存 time_complexity：O(n) space_complexity:O(n) 40ms 13.6mb
        new_l = []
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                new_l.append(0)
            else:
                digits[i] += 1
                return digits[0:i+1] + new_l
        return [1] + new_l


        # #纯递归 time_complexity：o(n),space_complexity:o(1) 36ms 13.6mb
        # if len(digits) == 0:
        #     return [1]
        # if  digits[-1] == 9:
        #     digits = self.plusOne(digits[0:-1]) + [0]
        #     return digits
        # else :
        #     digits [-1] += 1
        #     return digits
        # # #递归 + 缓存 time_complexity：o(n),space_complexity:o(n) 40ms 13.4mb
        # new_list = []
        # def help(list1):
        #     if len(list1) == 0:
        #        return [1] + new_list
        #     if list1[-1] == 9:
        #         new_list.append(0)
        #         return help(list1[:-1])
        #     else:
        #         list1[-1] += 1
        #         return list1+new_list
        # return help(digits)
        
        
        # # #类型转换 time_complexity：o(n) space_complexity:o(n) 36ms 13.7mb
        # # res = int(''.join(str(i) for i in digits)) + 1
        # # return [int(i) for i in str(res)]

        # # # # #尾指针遍历+指针记录 时间O（n）空间O（1）
        # # # # i = len(digits) - 1 
        # # # # tail = []
        # # # # while i >= 0 and digits[i] == 9:
        # # # #     i -= 1
        # # # #     tail.append(0)
        # # # # if i < 0:
        # # # #     return [1] + tail
        # # # # else:
        # # # #     digits[i] += 1
        # # # #     return digits[0:i+1] + tail

        # # # # # #尾指针遍历+指针记录 时间O（n）空间O（1）
        # # # # # i = l = len(digits) - 1 
        # # # # # while i >= 0 and digits[i] == 9:
        # # # # #     i -= 1
        # # # # # if i < 0:
        # # # # #     return [1] + [0] * (l - i)
        # # # # # else:
        # # # # #     digits[i] += 1
        # # # # #     return digits[0:i+1] + [0] * (l - i)

        # # # # # # #尾指针遍历+缓存 时间O（n）空间O（n）
        # # # # # # new_l = []
        # # # # # # for i in range(len(digits)-1,-1,-1):
        # # # # # #     if digits[i] == 9:
        # # # # # #         digits.pop()
        # # # # # #         new_l.append(0)
        # # # # # #     else:
        # # # # # #         digits[i] += 1
        # # # # # #         break
        # # # # # # if digits:
        # # # # # #     return digits + new_l
        # # # # # # else:
        # # # # # #     return [1] + new_l