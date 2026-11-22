class Solution {
    public int pivotIndex(int[] nums) { int tot=0; for(int x:nums) tot+=x; int l=0; for(int i=0;i<nums.length;i++){ if(l==tot-l-nums[i]) return i; l+=nums[i]; } return -1; }
}