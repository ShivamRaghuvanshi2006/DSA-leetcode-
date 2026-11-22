class Solution {
    public String[] uncommonFromSentences(String s1, String s2) { java.util.Map<String,Integer> m=new java.util.HashMap<>(); for(String w:(s1+" "+s2).split(" ")) m.put(w,m.getOrDefault(w,0)+1); java.util.List<String> r=new java.util.ArrayList<>(); for(var e:m.entrySet()) if(e.getValue()==1) r.add(e.getKey()); return r.toArray(new String[0]); }
}