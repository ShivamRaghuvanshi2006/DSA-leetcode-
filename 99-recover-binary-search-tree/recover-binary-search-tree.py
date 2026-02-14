class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # 'first' and 'second' are the nodes we need to swap
        # 'prev' tracks the node we just visited
        first = second = prev = None
        curr = root
        
        while curr:
            if curr.left is None:
                # --- Step 1: Check for the swap mistake ---
                if prev and prev.val > curr.val:
                    if not first: first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find the predecessor (rightmost node in left subtree)
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if pre.right is None:
                    # Create a temporary bridge back to 'curr'
                    pre.right = curr
                    curr = curr.left
                else:
                    # Bridge already exists; we are finished with left side
                    pre.right = None
                    
                    # --- Step 2: Check for the swap mistake (again) ---
                    if prev and prev.val > curr.val:
                        if not first: first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
        
        # Finally, swap the values of the two nodes we found
        if first and second:
            first.val, second.val = second.val, first.val