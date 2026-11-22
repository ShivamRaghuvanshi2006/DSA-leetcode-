class Solution {
 TreeNode cur;
 public TreeNode increasingBST(TreeNode root){TreeNode d=new TreeNode(0);cur=d; inorder(root); return d.right;}
 void inorder(TreeNode n){if(n==null)return; inorder(n.left); n.left=null; cur.right=n; cur=n; inorder(n.right);}
}