# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        #使用栈，time_complexity：o(n) space_complexity: o(n)
        stack , res = [(root,0)] , 0
        while stack:
            root, level = stack.pop()
            if root:
                level += 1
                res = max(level ,res)  
                if root.left:
                    stack.append((root.left,level))
                if root.right:
                    stack.append((root.right,level))
        return res














        #old

        # if not root : return 0
        # m , stack = 0 , [root]
        # while True:
        #     queue = []
        #     m += 1
        #     for i in stack:
        #         if i.left:
        #             queue.append(i.left)
        #         if i.right:
        #             queue.append(i.right)
        #     if any(queue):
        #         stack = queue.copy()
        #     else:
        #         return m
if __name__ == "__main__":
    for a in [x for j in range(3)  for x in range(2 * j)]:
        print(a)