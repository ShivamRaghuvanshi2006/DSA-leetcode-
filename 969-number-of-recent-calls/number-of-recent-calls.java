class RecentCounter {
 java.util.ArrayDeque<Integer> q=new java.util.ArrayDeque<>();
 public RecentCounter(){}
 public int ping(int t){ q.offer(t); while(q.peek()<t-3000) q.poll(); return q.size(); }
}