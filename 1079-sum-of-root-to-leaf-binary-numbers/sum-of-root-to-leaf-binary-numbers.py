class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            
            # Shift left and add current bit
            current_val = (current_val << 1) | node.val
            
            # If it's a leaf node, return the accumulated path value
            if not node.left and not node.right:
                return current_val
            
            # Sum the results from left and right subtrees
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)