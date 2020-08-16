class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._size = k
        self._queue = [None] * (k+2)
        self._front , self._last = 0 , 1


         
    def enTrue(self,n):
        if n < 0:
            n += self._size + 2
        if n > self._size + 1:
            n -= self._size + 2
        return n
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        #print('insertFront',self._queue,self._front,self._last)
        if self.isFull():
            return False
        self._queue[self._front] = value
        self._front = self.enTrue(self._front - 1)
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        #print('insertLast',self._queue,self._front,self._last)
        if self.isFull():
            return False
        self._queue[self._last] = value
        self._last = self.enTrue(self._last  + 1)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._queue[self._front] = None
        self._front = self.enTrue(self._front + 1)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._queue[self._last] = None
        self._last = self.enTrue(self._last - 1)
        return True
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._queue[self.enTrue(self._front + 1)]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._queue[self.enTrue(self._last - 1)]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self._last > self._front:
            return self._last  - self._front  == 1
        else:
            return self._last  + self._size + 2 - self._front  == 1
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self._last > self._front:
            return self._front + self._size + 2 - self._last  == 1
        else:
            return self._front - self._last  == 1


# Your MyCircularDeque object will be instantiated and called as such:
k = 3
value1 , value2 = 4, 5
obj = MyCircularDeque(k)
param_1 = obj.insertFront(value1)
param_2 = obj.insertLast(value2)

param_1 = obj.insertFront(value1)
param_2 = obj.insertLast(value2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()

print(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8)
