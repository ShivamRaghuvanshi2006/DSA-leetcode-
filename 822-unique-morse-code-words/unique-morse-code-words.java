class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] m = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        java.util.Set<String> se=new java.util.HashSet<>();
        for(String w:words){StringBuilder sb=new StringBuilder(); for(char c:w.toCharArray()) sb.append(m[c-97]); se.add(sb.toString());}
        return se.size();
    }
}