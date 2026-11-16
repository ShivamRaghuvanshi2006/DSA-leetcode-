class Solution:
    def sortedListToBST(self, head):
        arr=[]
        while head:
            arr.append(head.val); head=head.next
        def build(l,r):
            if l>r: return None
            m=(l+r)//2
            node=TreeNode(arr[m])
            node.left=build(l,m-1)
            node.right=build(m+1,r)
            return node
        return build(0,len(arr)-1)