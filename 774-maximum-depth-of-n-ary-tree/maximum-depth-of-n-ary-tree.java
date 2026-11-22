class Solution {
    public int maxDepth(Node root) { if(root==null) return 0; int m=0; if(root.children!=null) for(Node c: root.children) m=Math.max(m,maxDepth(c)); return m+1; }
}