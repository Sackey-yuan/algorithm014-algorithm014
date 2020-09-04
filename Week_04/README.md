学习笔记

使用分治递归解决问题的时候需要注意，修改的初始参数有时候需要还原：
如：
        def dfs(numlist,ans):
            # print(numlist,ans,res)
            l = len(numlist)
            if l > 0:
                for i in range(len(numlist)):
                    remain = numlist[0:i] if i+1 == l else numlist[0:i] + numlist[i+1:]
                    #dfs(remain,ans+[numlist[i]]) #fix
                    ans.append(numlist[i])
                    dfs(remain,ans) #导致ans被修改 改层的参数改变导致数据错误
            else:
                res.append(ans)
python库函数
itertools.permutations(List)#返回迭代对象 （List的全排序）

使用切片的时候List[n:] n可以大于list长度
# remain = numlist[0:i] if i + 1 == l else numlist[0:i] + numlist[i + 1:]
remain = numlist[0:i] + numlist[i+1:]
看不懂的写法：
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])
end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
python 库函数 双端队列 deque
start+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from collections import deque


d  = deque('1234556')
print(d) #deque(['1', '2', '3', '4', '5', '5', '6'])
d.appendleft('a')
d.append('b')
print(d) #deque(['a', '1', '2', '3', '4', '5', '5', '6', 'b'])
print(d.popleft())
#b
print(d.pop())
#6
print(d.pop())
#a
end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
python 字典使用技巧
start+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
hash_map = dict()
直接去key，使用get不存在的key返回None
hash_map.get(n)#None
hash_map[n]#报错
end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
python 浅拷贝问题 列表复制的是地址
ls = [["8"]*4]*4
lb = [["8"]*4 for _ in range(4)]
ls[1][1] = 's'
lb[1][1] = 's'
print('ls\n',ls)
#ls
# [['8', 's', '8', '8'],
#  ['8', 's', '8', '8'],
#  ['8', 's', '8', '8'],
#  ['8', 's', '8', '8']]

print('lb\n',lb)
#lb
# [['8', '8', '8', '8'],
#  ['8', 's', '8', '8'],
#  ['8', '8', '8', '8'],
#  ['8', '8', '8', '8']]