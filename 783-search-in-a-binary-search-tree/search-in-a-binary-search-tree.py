# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(curr,val):
            if not curr:
                return None
            if curr.val==val:
                return curr
            elif curr.val>val:
                return dfs(curr.left,val)
            else:
                return dfs(curr.right,val)


        return dfs(root, val)