class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int INF=Integer.MAX_VALUE/2;
        int[] dist=new int[n]; java.util.Arrays.fill(dist,INF); dist[src]=0;
        for(int i=0;i<=k;i++){int[] tmp=dist.clone();
            for(int[] f:flights){int u=f[0],v=f[1],w=f[2];
                if(dist[u]!=INF && tmp[v]>dist[u]+w) tmp[v]=dist[u]+w;}
            dist=tmp;}
        return dist[dst]>=INF?-1:dist[dst];
    }
}