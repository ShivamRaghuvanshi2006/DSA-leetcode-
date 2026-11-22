class Solution {
 public int numUniqueEmails(String[] emails){
  java.util.Set<String> s=new java.util.HashSet<>();
  for(String e:emails){
   int at=e.indexOf(64);
   String dom=e.substring(at);
   String loc=e.substring(0,at);
   int plus=loc.indexOf(43);
   if(plus>=0) loc=loc.substring(0,plus);
   StringBuilder b=new StringBuilder();
   for(int i=0;i<loc.length();i++){ char c=loc.charAt(i); if(c!=46) b.append(c); }
   s.add(b.toString()+dom);
  }
  return s.size();
 }
}