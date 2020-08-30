class Solution:
    """
    @param lengths: the lengths of sticks at the beginning.
    @return: return the minimum number of cuts.
    """
    def makeEquilateralTriangle(self, lengths):
        # write your code here.
        hash_map,res = {}, 2
        double = []
        m = max(lengths)
        for i in lengths:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
                if hash_map[i] == 3:
                    return 0
                else:
                    if m > i:
                        res = 1
            if i * 2 in hash_map or i / 2 in hash_map:
                res = 1
        return res

class Solution2:
    """
    @param s: a string.
    @return: return the values of all the intervals.
    """
    def suffixQuery(self, s):
        # write your code here
        hash_map = {}
        l = len(s)
        res = l
        for i in range(l):
            if s[i] not in hash_map:
                hash_map[s[i]] = [i]
            else:
                for j in hash_map[s[i]]:
                    left , right = j , i
                    while left < right:
                        res += 1
                        left, right = left+1, right-1
                        if s[left] != s[right]:
                            break
                hash_map[s[i]].append(i)
        return res
class Solution3:
    """
    @param heights: the heights of buildings.
    @param k: the vision.
    @param x: the energy to spend of the first action.
    @param y: the energy to spend of the second action.
    @return: the minimal energy to spend.
    """
    def shuttleInBuildings(self, heights, k, x, y):
        # write your code here.
        l = len(heights)
        res_list = []
        def help(i,res):
            if not res_list or res < min(res_list):
                if i == l-1:
                    res_list.append(res)
                else:
                    fa = i + k + 1 if i+ k + 1 < l else l
                    hight = heights[i]
                    next_i = i
                    for next_j in range(i + 1,fa):
                        if heights[next_j] > hight:
                            next_i, hight = next_j, heights[next_j]
                    if next_i > i:
                        help(next_i,res+x)
                    if i +1 < l :help(i + 1,res+y)
                    if i + 2 < l:help(i + 2,res+y)
        help(0,0)
        return min(res_list)




l  = [2,2,2,7]
# s = Solution()
# print(s.makeEquilateralTriangle(l))

strs = 'aaaaa'#5  aa:1 aaa:1 aaaa:2 aaaaa:2
# s2 = Solution2()
# print(s2.suffixQuery(strs))

heights = [1,5,4,3,3,5]
k = 3
x = 10
y = 6
# s3 = Solution3()
# print(s3.shuttleInBuildings(heights,k,x,y))
heights.sort()
import bisect
print(bisect.bisect(heights,3))
print(bisect.bisect(heights,4))
bisect.insort(heights,4)
print(heights)