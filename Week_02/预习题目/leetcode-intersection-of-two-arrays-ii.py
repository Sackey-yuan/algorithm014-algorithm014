class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #hash_map o(m+n) 64 ms	13.9 MB
        hash_map = {}
        for item in nums1:
            if item in hash_map:
                hash_map[item] += 1
            else:
                hash_map[item] = 1
        res = []
        for item in nums2:
            if item in hash_map:
                if hash_map[item] > 0:
                    res.append(item)
                    hash_map[item] -= 1
        return res

        
        #Counter() o(1) 52 ms	13.8 MB
        # c = Counter(nums1) & Counter(nums2)
        # return list(c.elements())