学习笔记
深度优先 广度优先
1、搜索就是暴力遍历所有节点
    1、保证效率每个节点访问一次
    2、树的搜索方法：深度优先、广度优先
深度优先搜索：
code one(二叉树）:
def dfs(node):
    if node in visited:
        #already visited
        return
    visited.add(node)
    #process current node
    dfs(node.left)
    dfs(node.right)

code two (多叉树)    
visited = set()
def dfs(node,visited):
    visited.add(node)
    #process current node here
    ...
    for nent_nod in node.children():
        if not next_node in visited:
            def(next_node, visited)
    
广度优先：
def bfs(graph, start, end):
    visited = set()
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
    #other processing work
    ...

贪心算法：
定义：
贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，算法得到的是在某种意义上的局部最优解。
贪心算法不是对所有问题都能得到整体最优解，关键是贪心策略的选择。也就是说，不从整体最优上加以考虑，做出的只是在某种意义上的局部最优解。
    1、不能回退，回溯
    2、只对当前子模块有最优解决方案
使用条件：
    1、一个问题的整体最优解可通过一系列的局部最优解的选择达到，并且每次的选择可以依赖之前的做出的选择，但不依赖以后面做出的选择。
对于一个具体问题，要确认证明一个问题是否可以使用贪心算法，必须证明每一步所做出的贪心选择最终会导致问题的整体最优解。
    3、当一个问题的最优解包含其子问题的最优解时，称此问题具有最优子结构性质。问题的最优子结构性质是该问题可用贪心法求解的关键所在。
在实际应用中，至于什么问题具有什么样的贪心选择性质是不确定的，需要具体问题具体分析。

二分查找：
1、队列是单调有序的
2、队列是有上下边界的
3、可以使用下标直接取值的

code：
left,right = 0, len(array) - 1
while left <= right:
    mid = left + (right - left)//2
    if array[mid] == target:
        #find the target!!!
        break or return mid
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
        
 

本周作业
简单：
柠檬水找零（亚马逊在半年内面试中考过） 已完成  lemonade-change.py
买卖股票的最佳时机 II （亚马逊、字节跳动、微软在半年内面试中考过）已完成 best-time-to-buy-and-sell-stock-ii.py
分发饼干（亚马逊在半年内面试中考过）
模拟行走机器人
使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
说明：同学们可以将自己的思路、代码写在第 4 周的学习总结中
中等：
单词接龙（亚马逊在半年内面试常考）
岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次） 已完成 Week_04/number-of-islands.py
扫雷游戏（亚马逊、Facebook 在半年内面试中考过）
跳跃游戏 （亚马逊、华为、Facebook 在半年内面试中考过）
搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）
搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过） 已完成 search-a-2d-matrix.py
寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）
困难
单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过）
跳跃游戏 II （亚马逊、华为、字节跳动在半年内面试中考过）





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