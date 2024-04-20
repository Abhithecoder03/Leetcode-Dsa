# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mini = float('inf')
        prev = float('-inf')
        def bst(root):
            nonlocal mini
            nonlocal prev
            if not root:
                return None
            bst(root.left)
            mini=min(mini,root.val-prev)
            prev=root.val
            bst(root.right)
        bst(root)
        return mini