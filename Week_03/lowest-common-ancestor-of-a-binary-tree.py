# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #递归 time_complexity：o（n）space_complexity：o（1）
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,q,p)
        right = self.lowestCommonAncestor(root.right,q,p)
        #one-line
        return root if left and right else left or right
        # if not left:return right
        # if not right:
        #     return left
        # return root