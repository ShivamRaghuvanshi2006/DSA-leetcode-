class Solution {
    public int numJewelsInStones(String jewels, String stones) { boolean[] s=new boolean[128]; for(char c:jewels.toCharArray()) s[c]=true; int a=0; for(char c:stones.toCharArray()) if(s[c]) a++; return a; }
}