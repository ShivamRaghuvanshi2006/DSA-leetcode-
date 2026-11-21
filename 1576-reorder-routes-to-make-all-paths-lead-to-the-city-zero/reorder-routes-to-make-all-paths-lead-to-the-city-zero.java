class Solution {
    public int minReorder(int n, int[][] connections) {
        java.util.List<int[]>[] g=new java.util.List[n];
        for(int i=0;i<n;i++) g[i]=new java.util.ArrayList<>();
        for(int[] c:connections){g[c[0]].add(new int[]{c[1],1}); g[c[1]].add(new int[]{c[0],0});}
        boolean[] vis=new boolean[n]; vis[0]=true;
        java.util.ArrayDeque<Integer> q=new java.util.ArrayDeque<>(); q.offer(0);
        int ans=0;
        while(!q.isEmpty()){int u=q.poll(); for(int[] nb:g[u]){int v=nb[0],w=nb[1]; if(!vis[v]){vis[v]=true; ans+=w; q.offer(v);}}}
        return ans;
    }
}