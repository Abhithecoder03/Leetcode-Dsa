# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree=TreeNode(None)
        dummy=tree
        def dfs(root):
            nonlocal dummy
            if not root:
                return None
            dfs(root.left)
            dummy.right=TreeNode(root.val)
            dummy=dummy.right
            dfs(root.right)
        dfs(root)
        return tree.right


        