# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=deque([])
        q.append(root)
        while q:
            level=len(q)
            curr=[]
            for i in range(level):
                ele=q.popleft()
                curr.append(ele.val)

                if ele.left is not None:
                    q.append(ele.left)
                if ele.right is not None:
                    q.append(ele.right)
            res.append(curr)
        return res


        