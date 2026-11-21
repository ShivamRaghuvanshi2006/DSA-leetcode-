class Solution {
    public int minCost(int maxTime, int[][] edges, int[] passingFees) {
        int n=passingFees.length;
        java.util.List<int[]>[] g=new java.util.List[n];
        for(int i=0;i<n;i++) g[i]=new java.util.ArrayList<>();
        for(int[] e:edges){g[e[0]].add(new int[]{e[1],e[2]}); g[e[1]].add(new int[]{e[0],e[2]});}
        int[][] minTime=new int[n][1001];
        // Dijkstra on (cost): dist time
        java.util.PriorityQueue<int[]> pq=new java.util.PriorityQueue<>((a,b)->a[0]-b[0]);
        pq.offer(new int[]{passingFees[0],0,0});
        int[] best=new int[n]; java.util.Arrays.fill(best,Integer.MAX_VALUE);
        while(!pq.isEmpty()){
            int[] c=pq.poll(); int cost=c[0],u=c[1],t=c[2];
            if(t>maxTime) continue;
            if(u==n-1) return cost;
            if(t>=best[u]) continue;
            best[u]=t;
            for(int[] nb:g[u]){int v=nb[0],w=nb[1]; int nt=t+w;
                if(nt>maxTime) continue;
                pq.offer(new int[]{cost+passingFees[v],v,nt});}
        }
        return -1;
    }
}