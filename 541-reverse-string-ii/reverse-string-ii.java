class Solution {
    public String reverseStr(String s, int k) {
        char[] a=s.toCharArray(); int n=a.length;
        for(int st=0;st<n;st+=2*k){ int l=st,r=Math.min(st+k-1,n-1); while(l<r){char t=a[l];a[l++]=a[r];a[r--]=t;} }
        return new String(a);
    }
}