学习笔记
周一：
isAnagram
sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

inorderTraversal
几种终结的写法
def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    if not root:
        return
    self.helper(root.left, res)
    res.append(root.val)
    self.helper(root.right, res)

周一
 两个数组的交集 II
intersection-of-two-arrays-ii
python 函数库：
Counter()
1、创建方法
>>> c = Counter()  # 创建一个空的Counter类
>>> c = Counter('adasdasd')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
>>> c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
>>> c = Counter(a=4, b=2)  # 从一组键值对创建
2、计数器更新（c.update(object)，c.subtract(object)）对象（list、tuple、dict、字符串等）
3、删除键  del c["a"]
4、 elements()返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。元素排列无确定顺序，个数小于1的元素不被包含。
list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
5、2.6 most_common([n])
返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。
6、浅拷贝copy  b = c.copy()
7、算术和集合操作
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d  # c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d  # subtract（只保留正数计数的元素）
Counter({'a': 2})
>>> c & d  # 交集:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d  # 并集:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})