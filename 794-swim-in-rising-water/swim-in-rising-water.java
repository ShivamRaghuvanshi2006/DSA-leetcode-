class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>((a, b) -> a[0] - b[0]);
        boolean[][] vis = new boolean[n][n];
        pq.offer(new int[]{grid[0][0], 0, 0});
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int t = cur[0], rr = cur[1], cc = cur[2];
            if (vis[rr][cc]) continue;
            vis[rr][cc] = true;
            if (rr == n - 1 && cc == n - 1) return t;
            for (int[] d : dirs) {
                int nr = rr + d[0], nc = cc + d[1];
                if (nr < 0 || nc < 0 || nr >= n || nc >= n || vis[nr][nc]) continue;
                pq.offer(new int[]{Math.max(t, grid[nr][nc]), nr, nc});
            }
        }
        return -1;
    }
}