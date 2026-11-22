class Solution {
    public int balancedStringSplit(String s) { int b=0,a=0; for(char c:s.toCharArray()){ if(c=='R') b++; else b--; if(b==0) a++; } return a; }
}