def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))