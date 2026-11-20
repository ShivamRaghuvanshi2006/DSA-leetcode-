class Solution {
    public boolean isAnagram(String s,String t){ if(s.length()!=t.length()) return false; int[] c=new int[26]; for(char x:s.toCharArray()) c[x-'a']++; for(char x:t.toCharArray()) if(--c[x-'a']<0) return false; return true; }
}