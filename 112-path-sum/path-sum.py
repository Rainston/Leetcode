# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetsum: int) -> bool:
        if not root:
            return False
        targetsum-=root.val
        if not root.left and not root.right:
            return targetsum==0
        return self.hasPathSum(root.left,targetsum) or self.hasPathSum(root.right,targetsum)