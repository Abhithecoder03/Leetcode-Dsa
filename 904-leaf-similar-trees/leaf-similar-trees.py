# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafele(curr,res):
            if not curr:
                return None
            if curr.left is None and curr.right is None:
                res.append(curr.val)
            leafele(curr.left,res)
            leafele(curr.right,res)
            return res

        return leafele(root1,[])==leafele(root2,[])