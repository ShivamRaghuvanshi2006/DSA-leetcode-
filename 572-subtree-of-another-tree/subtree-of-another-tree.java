class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) { if(s==null) return false; if(same(s,t)) return true; return isSubtree(s.left,t)||isSubtree(s.right,t); }
    boolean same(TreeNode a, TreeNode b){ if(a==null&&b==null) return true; if(a==null||b==null) return false; if(a.val!=b.val) return false; return same(a.left,b.left)&&same(a.right,b.right); }
}