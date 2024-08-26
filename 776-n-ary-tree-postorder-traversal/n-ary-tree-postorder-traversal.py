"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]
        def traverse(root):
            for i in root.children:
                traverse(i)
            res.append(root.val)
        traverse(root)
        return res