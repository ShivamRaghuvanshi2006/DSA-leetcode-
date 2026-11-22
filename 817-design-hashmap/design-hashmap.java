class MyHashMap {
    int[] m;
    public MyHashMap() { m=new int[1000001]; java.util.Arrays.fill(m,-1); }
    public void put(int key, int value) { m[key]=value; }
    public int get(int key) { return m[key]; }
    public void remove(int key) { m[key]=-1; }
}