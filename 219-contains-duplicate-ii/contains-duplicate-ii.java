class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        java.util.Map<Integer,Integer> last = new java.util.HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer prev = last.get(nums[i]);
            if (prev != null && i - prev <= k) return true;
            last.put(nums[i], i);
        }
        return false;
    }
}