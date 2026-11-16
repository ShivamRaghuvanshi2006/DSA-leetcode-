class Solution:
    def buildTree(self, inorder, postorder):
        idx={v:i for i,v in enumerate(inorder)}
        self.pi=len(postorder)-1
        def build(l,r):
            if l>r: return None
            v=postorder[self.pi]; self.pi-=1
            node=TreeNode(v)
            m=idx[v]
            node.right=build(m+1,r)
            node.left=build(l,m-1)
            return node
        return build(0,len(inorder)-1)