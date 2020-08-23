# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #循环遍历 time_complexity O(n) space_complexity: o(n) 44 ms	13.7 MB
        stack, res = [] , []
        while root or stack:
        # while True:
            while root:
                stack.append(root)
                root = root.left
            # if not  stack:
            #     return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

        # #递归 time_complexity:o(n) 52 ms	13.8 MB space_complexity:o(log n)->o(n)
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