class Solution {
    public int findShortestSubArray(int[] nums) { java.util.Map<Integer,int[]> m=new java.util.HashMap<>(); int deg=0; for(int i=0;i<nums.length;i++){ int v=nums[i]; m.putIfAbsent(v,new int[]{i,i,0}); int[] a=m.get(v); a[1]=i; a[2]++; deg=Math.max(deg,a[2]); } int ans=nums.length; for(int[] a: m.values()) if(a[2]==deg) ans=Math.min(ans,a[1]-a[0]+1); return ans; }
}