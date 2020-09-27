学习笔记
1.Trie 
``` python
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_od_word in node
    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```
2.并查集
```python
def init(p, n):
    # for i in range(n): p[i] = i
    p = [i for i in range(n)]

def union(self, p, i, j):
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] == root:
        root = p[root]
    while p[i] != i:
        x = i
        i = p[i]
        p[x] = root
    return root
```
3.DFS
递归写法
```python 
#递归写法
visited = set()
def dfs(node, visited):
    if node in visited: #terminator
        #visited
        return
    visited(node)
    #process current node here.
    ...
    for next_node in node.children:
        dfs(next_node, visited)
```
非递归写法
```python
#python 非递归写法
def dfs(self, tree):
    if not tree:
        return []
    visited, stack = set(), [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        #process(node)
        nodes = generate_related_node(node)
        stack.push(nodes)

def generate_related_node(node):
    pass
```
4.bfs
```python
def bfs(node):
    visited = set()
    queue = [node]
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_node(node)
        queue.push(nodes)
        
def generate_related_node(node):
    pass

def process(node):
    pass
        

```
5、双向bfs
```python
def de_bfs(start, end):
    left_stack, right_stack = set(), set()
    left_stack.add(start)
    right_stack.add(end)
    while left_stack and right_stack:
        if len(left_stack) < len(right_stack):
            left_stack, right_stack = right_stack, left_stack
        next_stack = set()
        for item in left_stack:
            next_item = process(item)
            if next_item in right_stack:
                return #result
            next_stack.add(next_item)
        left_stack = next_stack

def process(item):
    return item.next    
```
