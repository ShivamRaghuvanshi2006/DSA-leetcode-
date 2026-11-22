class Solution {
    public int[][] transpose(int[][] m) { int r=m.length,c=m[0].length; int[][] a=new int[c][r]; for(int i=0;i<r;i++) for(int j=0;j<c;j++) a[j][i]=m[i][j]; return a; }
}