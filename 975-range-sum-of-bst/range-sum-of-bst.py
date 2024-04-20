# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_Range=0
        def traverse(root,low,high):
            nonlocal sum_Range
            if not root:
                return None
            traverse(root.left,low,high)
            if root.val>=low and root.val<=high:
                sum_Range+=root.val
            traverse(root.right,low,high)
        traverse(root,low,high)
        return sum_Range


        