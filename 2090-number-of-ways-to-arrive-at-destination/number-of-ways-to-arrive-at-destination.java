class Solution {
    public int countPaths(int n, int[][] roads) {
        java.util.List<long[]>[] g=new java.util.List[n];
        for(int i=0;i<n;i++) g[i]=new java.util.ArrayList<>();
        for(int[] r:roads){g[r[0]].add(new long[]{r[1],r[2]}); g[r[1]].add(new long[]{r[0],r[2]});}
        long[] dist=new long[n]; java.util.Arrays.fill(dist,Long.MAX_VALUE); dist[0]=0;
        long[] ways=new long[n]; ways[0]=1;
        java.util.PriorityQueue<long[]> pq=new java.util.PriorityQueue<>((a,b)->Long.compare(a[0],b[0]));
        pq.offer(new long[]{0,0});
        long MOD=1000000007;
        while(!pq.isEmpty()){long[] c=pq.poll(); long d=c[0]; int u=(int)c[1];
            if(d>dist[u]) continue;
            for(long[] nb:g[u]){int v=(int)nb[0]; long w=nb[1]; long nd=d+w;
                if(nd<dist[v]){dist[v]=nd; ways[v]=ways[u]; pq.offer(new long[]{nd,v});}
                else if(nd==dist[v]){ways[v]=(ways[v]+ways[u])%MOD;}}}
        return (int)(ways[n-1]%MOD);
    }
}