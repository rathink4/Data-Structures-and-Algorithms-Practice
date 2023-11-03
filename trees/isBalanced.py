def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root: return True
    
    ld = self.depth(root.left)
    rd = self.depth(root.right)
    if abs(ld-rd) > 1: return False
    
    return self.isBalanced(root.left) and self.isBalanced(root.right)

def depth(self, root):
    if not root: return 0
    return max(1+self.depth(root.left), 1+self.depth(root.right))