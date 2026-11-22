class Solution {
 public boolean hasGroupsSizeX(int[] deck){ java.util.Map<Integer,Integer> m=new java.util.HashMap<>(); for(int x:deck)m.put(x,m.getOrDefault(x,0)+1); int g=0; for(int v:m.values()) g=gcd(g,v); return g>=2; }
 int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
}