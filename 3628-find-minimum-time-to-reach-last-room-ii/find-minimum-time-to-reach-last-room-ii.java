class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int n=moveTime.length,m=moveTime[0].length;
        int[][] dist=new int[n][m];
        for(int i=0;i<n;i++) java.util.Arrays.fill(dist[i],Integer.MAX_VALUE);
        dist[0][0]=0;
        java.util.PriorityQueue<int[]> pq=new java.util.PriorityQueue<>((a,b)->a[0]-b[0]);
        pq.offer(new int[]{0,0,0});
        int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
        while(!pq.isEmpty()){
            int[] c=pq.poll(); int t=c[0],r=c[1],cc=c[2];
            if(t!=dist[r][cc]) continue;
            if(r==n-1&&cc==m-1) return t;
            int step=((r+cc)%2==0)?1:2;
            for(int[] d:dirs){int nr=r+d[0],nc=cc+d[1];
                if(nr<0||nc<0||nr>=n||nc>=m) continue;
                int nt=Math.max(t,moveTime[nr][nc])+step;
                if(nt<dist[nr][nc]){dist[nr][nc]=nt; pq.offer(new int[]{nt,nr,nc});}}
        }
        return -1;
    }
}