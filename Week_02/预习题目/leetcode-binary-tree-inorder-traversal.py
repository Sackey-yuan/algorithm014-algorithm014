#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        #使用栈
        stack, res = [] , []
        while root or stack:
            while root:
                stack.append(root.left)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        
        
        # #递归 time_complexity:o(n)
        # if not root:
        #     return []
        # res = []
        # def help_inorderTraversal(root):
        #     if not root:
        #         return
        #     help_inorderTraversal(root.left)
        #     res.append(root.val)
        #     help_inorderTraversal(root.right)
        # help_inorderTraversal(root)
        # return res