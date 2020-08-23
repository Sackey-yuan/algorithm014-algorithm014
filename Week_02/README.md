学习笔记
周一：
leetcode-valid-anagram.py
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

inorderTraversal
几种递归终结的写法
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

python装饰器：
装饰器：修改函数的功能的函数
1、python中一切皆对象，包括函数
2、在函数中可以定义函数
3、在函数中可以返回函数
def help():
    def print_holle():
        print("holle")
        return "ho"
    return print_holle
a = help()
print(a)  #output:<function greet at 0x121424323423>
print(a()) #output: holle \n ho
4、可以将函数作为参数传给另一个函数

5、@wraps(a_func)用来在修改函数的时候保证名不变；实现逻辑是只用a_func函数的函数名和注释覆盖修改的后的函数
6、使用场景列举：
a、授权：
    装饰器能有助于检查某个人是否被授权去使用一个web应用的端口。例如在Flask和Django web框架中
form functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = request.aurhorization
        if not auth or not chech_auth(auth.username,auth.password):
            authenticate()
        return f(*ags,**kwargs)
    return decorated
 
b、打印日志：
form functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__+"was called")
        retur func(*args,**kwargs)
    return with_logging

@logit
def addition_func(x):
    """do some math."""
    return x + x

result = addition_func(4)
#Out put:addition_func was called.

7、带参数的装饰器#同函数参数一致
8、装饰器的类
fron functools import wraps

class logit(obiect):
    def __init__(self,logfile="out.log")
        self.logfile = logfile
    
    def __call__(self,func):
        @wraps(func)
        def wrapped_func(*args, **kwrags):
            log_string = func.__name__ + "was called ."
            print(log_string)
            with open(self.logfile) as open_file:
                open_file.write(log_string + "\n")
            self.notify()
            return func(*args, **kwargs)
        return wrapped_funct
    
    def notify(self):
        #logit 只打印日志，不做别的or 自己想添加的do something
        pass
复用装饰类实现打印同时发邮件
class enail_logit(logit):
    def __init__(self, email = "admin@myproject.com",*args, **kwargs:
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)
    
    def notify(self):
        #email
        pass


周五：
https://leetcode-cn.com/problems/add-digits/
python3
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0 #python中（-1）%9是8  不是-1 go 中结果是-8
        return (num - 1 ) % 9 + 1
        
        # while num > 9:
        #     num = num % 10 + num // 10
        # return num

周六：
递归代码做优化的时候把结算放入了return中，可以是代码比较简洁
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #递归：time_complexity：o(n) space_complexity: o(1) 开率递归空间o(n)52 ms	15.7 MB
        if root:
            #return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 #代码优化 56 ms	15.5 MB
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            level = max(left,right) + 1
            return level
        return 0

python空值的一些问题：

在数据处理的过程中，经常会遇到数据为空的情况，然后踩到很多坑浪费很久的时间，今天总结一下Python中空值的情况，以防后续再掉进坑里。
Python中空值一般有四种情况，None," ",False和NaN:
前三种类型中 打印 None == None ," " == " " ,False == False都能返回判断True,但是np.NaN == np.NaN 却返回为False：
要创建一个空值可以用np.NaN,而且type(np.NaN)是float类型，而type(None)是NoneType类型，type(" ")是字符串类型，而在pandas中的数据类型例如Series和DataFrame中如果数组中除了空值之外全部是数值类型则None会转化正NaN

在Series或者DataFrame整体判断是否为空时，用isnull()，返回一个布尔型的矩阵；而且只有None 和NaN才被判断为空值

要是判断某一列中有空值存在，可以使用isnull().any()：

当判断单个值是否为空时，要用np.isnan()，但是np.isnan()只能用于数值型，NaN是Not a Number的缩写；其他类型可以用type(x).__name__ == 'float'来判断是否为空值，也可以利用np.NaN != np.NaN的特性来判断（即自身不等于自身时，该值为空值），这些方法只适用于空值为NaN类型的，当空值类型为None时，可以使用type(x) .__name__ == 'NoneType'来判断

可以用data[data.isnull().values==True]来筛选含有空值的行，但是如果某行有多个值是空值，则会重复次数出现，所以利用data[data.isnull().values==True].drop_duplicates()来去重：

为了将空值统一格式处理，可以在读取数据是限制一下，read_csv(na_values='NULL')将空值统一成NaN处理。

Python2中sum()函数对于NaN+NaN计算结果为NaN
Python3中sum()函数对于NaN+NaN计算结果为0
如果需要在Python3中使用sum()函数，对于NaN+NaN计算结果为NaN，该怎么处理呢？
Python3中sum()函数增加一个参数即可
#python3中增加参数min_count
min_count=1表示多个数求和过程中至少有1个及以上非空数据,否则返回NaN,
df[‘signal’] = df[[‘signal_long’,‘signal_short’]].sum(axis=1,min_count=1)

相关问题微博：python None 和 NaN
https://www.cnblogs.com/Allen-rg/p/9664844.html

来自简书：
Python3 - 无穷大与NaN
https://www.jianshu.com/p/3731d70658f6

创建或测试正无穷(inf)、负无穷(-inf)或NaN等非数字的浮点数
a = float('-inf') #负无穷
b = float('inf') #正无穷
C = float('nan') #空

周日：
查看标准堆的代码和自己写的进行对比，收获如下：
1、可以封账在一个函数里多次使用的代码一定要封装，方便复用
2、尽可能细化问题点（同样也有利于封装复用）
3、代码末尾使用 if __name__ == "__main__":模块存放测试用例：良好的测试喜欢

N叉树的层序遍历python3广度优先搜索算法
[]中间的for循环嵌套  
[children for node in queue for children in node.children]
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res,queue = [],[root]
        while queue:
            res.append([node.val for node in queue])
            queue = [children for node in queue for children in node.children]
        return res







本周作业：
二叉树的中序遍历（亚马逊、微软、字节跳动在半年内面试中考过）
二叉树的前序遍历（谷歌、微软、字节跳动在半年内面试中考过）
N 叉树的后序遍历（亚马逊在半年内面试中考过）
N 叉树的前序遍历（亚马逊在半年内面试中考过）
N 叉树的层序遍历
实战例题
最小的 k 个数（字节跳动在半年内面试中考过）
滑动窗口最大值（亚马逊在半年内面试中常考）
课后作业
HeapSort ：自学 https://www.geeksforgeeks.org/heap-sort/
丑数（字节跳动在半年内面试中考过）
前 K 个高频元素（亚马逊在半年内面试中常考）

