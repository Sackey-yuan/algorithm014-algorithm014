# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #time_complexity:O(n) space_complexity:o(n)
        def myBuildTree(pre_left,pre_right,inorder_left, inorde_right):
            if pre_left > pre_right:
                return None
            pre_root = preorder[pre_left]
            inorder_root  = hash_index[pre_root]
            pre_size = inorder_root - inorder_left
            root = TreeNode(pre_root)
            root.left = myBuildTree(pre_left+1,pre_left + pre_size,inorder_left,inorder_root -1)
            root.right = myBuildTree(pre_left+pre_size+1,pre_right,inorder_root+1,inorde_right)
            return root
        n = len(preorder)
        hash_index = {item:i for i,item in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)

