class Solution {
    public boolean leafSimilar(TreeNode a, TreeNode b) { java.util.List<Integer> x=new java.util.ArrayList<>(),y=new java.util.ArrayList<>(); dfs(a,x); dfs(b,y); return x.equals(y); }
    void dfs(TreeNode n, java.util.List<Integer> l){ if(n==null) return; if(n.left==null&&n.right==null) l.add(n.val); dfs(n.left,l); dfs(n.right,l); }
}