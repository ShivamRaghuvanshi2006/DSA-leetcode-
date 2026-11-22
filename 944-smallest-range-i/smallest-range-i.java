class Solution {
 public int smallestRangeI(int[] nums, int k){int mn=10000,mx=0; for(int x:nums){mn=Math.min(mn,x);mx=Math.max(mx,x);} return Math.max(0,mx-mn-2*k);}
}