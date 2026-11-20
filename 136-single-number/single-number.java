class Solution {
    public int singleNumber(int[] n){ int r=0; for(int x:n) r^=x; return r; }
}