import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] n){ Set<Integer> s=new HashSet<>(); for(int x:n) if(!s.add(x)) return true; return false; }
}