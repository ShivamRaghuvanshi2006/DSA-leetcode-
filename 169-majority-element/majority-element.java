class Solution {
    public int majorityElement(int[] n){ int c=0,cnt=0; for(int x:n){ if(cnt==0) c=x; cnt+= (x==c?1:-1);} return c; }
}