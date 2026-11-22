class Solution {
    int ans=0;
    public int findTilt(TreeNode root) { sum(root); return ans; }
    int sum(TreeNode n){ if(n==null) return 0; int l=sum(n.left),r=sum(n.right); ans+=Math.abs(l-r); return l+r+n.val; }
}