# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(curr,val,depth):
            if not curr:
                return 0
            if depth==2:
                curr.left=TreeNode(val ,left=curr.left)
                curr.right=TreeNode(val,right=curr.right)
                return
            dfs(curr.left,val,depth-1)
            dfs(curr.right,val,depth-1)
        if depth==1:
            return TreeNode(val,root)
        dfs(root,val,depth)
        return root
        