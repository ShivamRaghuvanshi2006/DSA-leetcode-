class Solution {
    public java.util.List<String> summaryRanges(int[] nums) {
        java.util.List<String> res = new java.util.ArrayList<>();
        int i=0,n=nums.length;
        while(i<n){ int s=nums[i]; while(i+1<n && nums[i+1]==nums[i]+1) i++; if(nums[i]==s) res.add(String.valueOf(s)); else res.add(s+"->"+nums[i]); i++; }
        return res;
    }
}