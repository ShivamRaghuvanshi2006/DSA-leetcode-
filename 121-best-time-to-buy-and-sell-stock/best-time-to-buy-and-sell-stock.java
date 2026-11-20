class Solution {
    public int maxProfit(int[] p){ int mn=Integer.MAX_VALUE,best=0; for(int x:p){ mn=Math.min(mn,x); best=Math.max(best,x-mn);} return best; }
}