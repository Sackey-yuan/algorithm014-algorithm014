from typing  import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #time_complexity:o(n) space_complexity:o(n + logn )
        if not root: return []
        res,queue = [],[root]
        while queue:
            res.append([node.val for node in queue])
            queue = [children for node in queue for children in node.children]
        return res



        # if not root:
        #     return []
        # stack ,res =[root], []
        # while stack:
        #     rstack,leval = [],[]
        #     for a in stack:
        #         if a:
        #             leval.append(a.val)
        #             rstack.extend([i for i in a.children])
        #     stack = rstack
        #     res.append(leval)
        # return res