class Solution {
    public int projectionArea(int[][] g) { int n=g.length,a=0; for(int i=0;i<n;i++) for(int j=0;j<n;j++){ if(g[i][j]>0) a++; } for(int i=0;i<n;i++){int mr=0,mc=0; for(int j=0;j<n;j++){mr=Math.max(mr,g[i][j]); mc=Math.max(mc,g[j][i]);} a+=mr+mc;} return a; }
}