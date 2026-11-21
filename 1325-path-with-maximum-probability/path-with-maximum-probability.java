class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        java.util.List<double[]>[] g=new java.util.List[n];
        for(int i=0;i<n;i++) g[i]=new java.util.ArrayList<>();
        for(int i=0;i<edges.length;i++){int a=edges[i][0],b=edges[i][1]; double p=succProb[i];
            g[a].add(new double[]{b,p}); g[b].add(new double[]{a,p});}
        double[] best=new double[n]; best[start_node]=1.0;
        java.util.PriorityQueue<double[]> pq=new java.util.PriorityQueue<>((x,y)->Double.compare(y[0],x[0]));
        pq.offer(new double[]{1.0,start_node});
        while(!pq.isEmpty()){double[] c=pq.poll(); double p=c[0]; int u=(int)c[1];
            if(p<best[u]-1e-12) continue;
            if(u==end_node) return p;
            for(double[] nb:g[u]){int v=(int)nb[0]; double np=p*nb[1];
                if(np>best[v]){best[v]=np; pq.offer(new double[]{np,v});}}}
        return 0.0;
    }
}