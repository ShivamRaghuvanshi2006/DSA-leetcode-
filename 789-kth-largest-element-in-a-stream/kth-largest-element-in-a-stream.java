class KthLargest {
    int k; java.util.PriorityQueue<Integer> pq=new java.util.PriorityQueue<>();
    public KthLargest(int k, int[] nums) { this.k=k; for(int x:nums) add(x); }
    public int add(int val) { pq.offer(val); if(pq.size()>k) pq.poll(); return pq.peek(); }
}