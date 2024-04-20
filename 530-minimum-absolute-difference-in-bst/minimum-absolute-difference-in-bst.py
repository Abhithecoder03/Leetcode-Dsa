# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini=float('inf')
        prev=float('inf')
        def dfs(root):
            nonlocal mini
            nonlocal prev
            if not root:
                return None
            dfs(root.left)
            mini=min(mini,abs(root.val-prev))
            prev=root.val
            dfs(root.right)
        dfs(root)
        return mini
        
        