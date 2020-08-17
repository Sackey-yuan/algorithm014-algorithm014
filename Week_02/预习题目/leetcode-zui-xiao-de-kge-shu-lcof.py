from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #使用max（）建立查询表 O（k+n）
        maps = [0] * (max(arr) + 1)
        res = []
        for i in arr:
            maps[i] += 1
        now = 0
        for i in maps:
            if maps[i]:
                if maps[i] + now >= k:
                    res.extend([i] * k-now)
                    
                else:
                    res.extend([i] * maps[i])
                    now += maps[i]
        return res

        # #快速排序  o(log n) 60 ms	14.7 MB
        # arr.sort()
        # return arr[:k]