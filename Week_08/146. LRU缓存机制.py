class LRUCache:
    """库函数 collections.OrderedDict"""
    def __init__(self,  capacity: int):
        self.hash_map = collections.OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.hash_map:
            self.hash_map.move_to_end(key)
            return self.hash_map[key]
        return -1
    
    def put(self, key, value):
        if self.get(key) == -1:
            if len(self.hash_map) == self.capacity:
                self.hash_map.popitem(last=False)
        self.hash_map[key] = value  

# class Note:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.pre = None
#         self.next = None


# class LRUCache:
#   """双向连表 +  hash_map"""
#     def __init__(self,  capacity: int):
#         self.hash_map = collections.OrderedDict()
#         self.capacity = capacity
    
#     def get(self, key):
#         if key in self.hash_map:
#             self.hash_map.move_to_end(key)
#             return self.hash_map[key]
#         return -1

#     def put(self, key, value):
#         if self.get(key) == -1:
#             if len(self.hash_map) == self.capacity:
#                 self.hash_map.popitem(last=False)
#         self.hash_map[key] = value

# #     def __init__(self, capacity: int):
# #         # self.map = set()
# #         # self.head = None
# #         self.tail = None
# #         self.queue = {}
# #         self.limit = capacity
# #         self.len_queue = 0

# #     def get(self, key: int) -> int:
# #         if key in self.queue:
# #             res = self.queue[key].value
# #             self.remove(key)
# #             self.add(key, res)
# #             # print(self.queue)
# #             # print(self.head)
# #             # print(self.tail)
# #             return res
# #         return -1

# #     def remove(self, key):
# #         res = self.queue[key]
# #         if key != self.head and key != self.tail:
# #             res.pre.next = res.next  
# #             res.next.pre = res.pre    
# #         elif key == self.head and key == self.tail :
# #             self.head = None
# #             self.tail = None
# #         elif key == self.tail :
# #             res.pre.next = res.next
# #             self.tail = res.pre.key
# #         else:# res.pre is None:
# #             res.next.pre = None
# #             self.head = res.next.key
# #         # res.pre.next = res.next
# #         self.len_queue -= 1
# #         del self.queue[key]

# #     def add(self, key, value):
# #         if self.len_queue >= self.limit:
# #             self.remove(self.tail)
# #         new_note = Note(key, value)
# #         self.queue[key] = new_note
# #         if self.head == None:
# #             self.head = key
# #             self.tail = key
# #         else:
# #             new_note.next = self.queue[self.head]
# #             self.queue[self.head].pre = new_note
# #             self.head = key
# #         self.len_queue += 1

# #     def put(self, key: int, value: int) -> None:
# #         # print(self.queue)
# #         if key in self.queue :
# #             self.remove(key)
# #         self.add(key, value)
         


# # # Your LRUCache object will be instantiated and called as such:
# # # obj = LRUCache(capacity)
# # # param_1 = obj.get(key)
# # # obj.put(key,value)