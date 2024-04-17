class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # Initialize the smallest variable to a placeholder that would be greater than any possible result
        self.smallest = '~'  # Use a very high value in the lexicographic order
        
        def dfs(node, path):
            if not node:
                return
            
            # Build path from leaf to root (reverse order)
            current_path = chr(node.val + ord('a')) + path
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                # Compare the current path with the smallest found so far
                if current_path < self.smallest:
                    self.smallest = current_path
            
            # Recursive DFS call for left and right child
            dfs(node.left, current_path)
            dfs(node.right, current_path)

        # Start DFS from the root with an empty path
        dfs(root, "")
        
        # Reverse the string to present it from root to leaf
        return self.smallest

# Example Usage
# root = TreeNode(0, TreeNode(1), TreeNode(2))
# sol = Solution()
# print(sol.smallestFromLeaf(root))  # Should print the smallest string from root to leaf
