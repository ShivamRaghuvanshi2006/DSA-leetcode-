class Solution {
    public int surfaceArea(int[][] g) { int n=g.length,a=0; for(int i=0;i<n;i++) for(int j=0;j<n;j++){ if(g[i][j]>0){a+=2; if(i==0) a+=g[i][j]; else a+=Math.max(0,g[i][j]-g[i-1][j]); if(i==n-1) a+=g[i][j]; else a+=Math.max(0,g[i][j]-g[i+1][j]); if(j==0) a+=g[i][j]; else a+=Math.max(0,g[i][j]-g[i][j-1]); if(j==n-1) a+=g[i][j]; else a+=Math.max(0,g[i][j]-g[i][j+1]);}} return a; }
}