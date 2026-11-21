class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] d=new int[n][n];
        for(int i=0;i<n;i++){java.util.Arrays.fill(d[i],1000000000); d[i][i]=0;}
        for(int[] e:edges){d[e[0]][e[1]]=e[2]; d[e[1]][e[0]]=e[2];}
        for(int k=0;k<n;k++) for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(d[i][j]>d[i][k]+d[k][j]) d[i][j]=d[i][k]+d[k][j];
        int ans=0,best=Integer.MAX_VALUE;
        for(int i=0;i<n;i++){int c=0; for(int j=0;j<n;j++) if(d[i][j]<=distanceThreshold) c++;
            if(c<=best){best=c; ans=i;}}
        return ans;
    }
}