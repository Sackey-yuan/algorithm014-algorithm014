#优秀代码积累：
************************************************************************************
#列表中的for循环嵌套
************************************************************************************
[Item for secondlist in firestList for Item in secondList]
例如：print([x for j in range(3) for i in range(j * 2) for x in range(2 * i)])
# j :0 , 1,          2
# i :    0 , 1,      0, 1,      2,            3,
# x :        0, 1,       0, 1,  0, 1, 2, 3,   0, 1, 2, 3, 4, 5
#[           0, 1,       0, 1,  0, 1, 2, 3,   0, 1, 2, 3, 4, 5]
*************************************************************************************
#堆的python实现
************************************************************************************
import  sys

class Binaryheap:

    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.Heap = [0] * (self.capacity)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return 2 * pos + 1
    
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

    def heapifyDown(self, pos):

    def insert(self, slement):

    def Print(self):

    def minHeap(self):

    def delete(self):

    def isEmpty(self):

    def isFull(self):

if __name__ == "__main__":
    print('The minHeap is')
    minHeap = BinaryHeap(5)
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.delete())) 

************************************************************************************
    获取数字的符号
************************************************************************************
flag = int(n >= 0) - int(n<0)

************************************************************************************
计算幂运算：取二进制末尾数:  n&1 二进制移位运算： n >>= 1
************************************************************************************
flag = int(n >= 0) - int(n<0)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #iterative
        if n < 0:
            x , n = 1/x , -n
        pow  = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

************************************************************************************
二分查找模块
************************************************************************************
#import besect
i = besect.besect(nums_list,num,lo=0,hi=None)#返回any in nums_list[:i] <= num, any in nums_list[i:] > num :lo,hi 是二分查找的初始坐标
besect。insort(nums_list,item,lo=0,hi=None)#二分查找插入item
####################################################################################
