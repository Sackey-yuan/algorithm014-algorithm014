class Solution:
    def climbStairs(self, n: int) -> int:
        #mathematical formal
        return int((1/pow(5,0.5))*(pow((1+pow(5,0.5))/2,n+1)-pow((1-pow(5,0.5))/2,n+1)))
                
        
        # #ditui
        # n1 , n2 = 1 , 1
        # for i in range(n-1):
        #     n1 , n2 = n1+ n2 , n1
        # return n1
        
        
        # # #递归+ 缓存
        # # hash_map = {1:1, 0:1}
        # # def help(n):
        # #     if n in hash_map:
        # #         return hash_map[n]
        # #     n1 = help(n-1)
        # #     n2 = help(n-2)
        # #     hash_map[n] = n1+ n2
        # #     return hash_map[n]
        # # return help(n)






        # # # #递归+缓存 time_complexity：o:（n）space_complexity:O(n)
        # # # hash_map = {1:1,0:1}
        # # # def help(n):
        # # #     if n in hash_map:
        # # #         return hash_map[n]
        # # #     else:
        # # #         n_1 = help(n-1)
        # # #         n_2 = help(n-2)
        # # #         hash_map[n] = n_1 + n_2
        # # #         return hash_map[n]
        # # # return help(n)
        

        # # # # #数学公式 O(1) 28ms
        # # # # res = (1/ pow(5,0.5)) *(pow(((1+pow(5,0.5))/2),(n+1))-pow(((1-5**0.5)/2),(n+1)))
        # # # # return int(res)
        # # # # # #矩阵计算 #108 ms
        # # # # # import numpy as np
        # # # # # res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), n) * np.matrix([[1], [0]])
        # # # # # return int(res[0][0])

        # # # # # #生成器发时间o(n),空间o(1) #44 ms
        # # # # # def fib_yield():
        # # # # #     a,b = 1,1
        # # # # #     while True:
        # # # # #         yield a
        # # # # #         a, b = a + b , a
        # # # # # res = 1
        # # # # # f = fib_yield()
        # # # # # for i in range(n):
        # # # # #     res = next(f)
        # # # # # return res

        # # # # # # # # # #顺序推导o(n)
        # # # # # # # # # if n < 3 :
        # # # # # # # # #     return n
        # # # # # # # # # res, f1  = 3 , 2
        # # # # # # # # # for i in range(n - 3):
        # # # # # # # # #     res, f1  = f1 + res , res
        # # # # # # # # # return res