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



