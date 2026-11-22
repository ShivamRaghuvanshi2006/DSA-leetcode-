class MyHashSet {
    boolean[] s=new boolean[1000001];
    public MyHashSet() {}
    public void add(int key) { s[key]=true; }
    public void remove(int key) { s[key]=false; }
    public boolean contains(int key) { return s[key]; }
}