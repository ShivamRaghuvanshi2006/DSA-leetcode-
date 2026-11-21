class Solution {
    public int minimumEffortPath(int[][] heights) {
        int R = heights.length, C = heights[0].length;
        int[][] dist = new int[R][C];
        for (int i = 0; i < R; i++) java.util.Arrays.fill(dist[i], Integer.MAX_VALUE);
        dist[0][0] = 0;
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>((a,b)->a[0]-b[0]);
        pq.offer(new int[]{0,0,0});
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            int e=cur[0], r=cur[1], c=cur[2];
            if(e!=dist[r][c]) continue;
            if(r==R-1 && c==C-1) return e;
            for(int[] d:dirs){
                int nr=r+d[0], nc=c+d[1];
                if(nr<0||nc<0||nr>=R||nc>=C) continue;
                int ne = Math.max(e, Math.abs(heights[nr][nc]-heights[r][c]));
                if(ne<dist[nr][nc]){dist[nr][nc]=ne; pq.offer(new int[]{ne,nr,nc});}
            }
        }
        return 0;
    }
}