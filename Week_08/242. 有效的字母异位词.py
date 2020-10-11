class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #online 2
        return sorted(s) == sorted(t)


        # #使用hash_map 遍历字符串  优化 time_complexity:O(n)
        # if len(s) != len(t):
        #     return False
        # hash_map = {}
        # for i in range(len(s)):
        #     hash_map[s[i]] = hash_map.get(s[i],0) + 1
        #     hash_map[t[i]] = hash_map.get(t[i],0) - 1
        # if any(hash_map.values()):
        #     return False
        # return True


        # # #online 48 ms	13.9 MB
        # # return Counter(s) == Counter(t)

        # # # #使用hash_map 遍历字符串 time_complexity:O(n) 84 ms	13.9 MB
        # # # if len(s) != len(t):
        # # #     return False
        # # # hash_map = {}
        # # # for i in s:
        # # #     if i in hash_map:
        # # #         hash_map[i] += 1
        # # #     else:
        # # #         hash_map[i] = 1
        # # # for i in t:
        # # #     if i in hash_map and hash_map[i] > 0 :
        # # #         hash_map[i] -= 1
        # # #     else:
        # # #         return False
        # # # return True


        # # # # #使用库函数 time_complexity：o(1)
        # # # # if len(s) != len(t):
        # # # #     return False
        # # # # l = len(s)
        # # # # s , g = Counter(s),Counter(t)
        # # # # return sum((s & g).values()) == l