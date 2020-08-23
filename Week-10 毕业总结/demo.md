#优秀代码积累：
#堆的python实现
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
