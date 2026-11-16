from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.c=capacity; self.od=OrderedDict()
    def get(self, key):
        if key not in self.od: return -1
        self.od.move_to_end(key); return self.od[key]
    def put(self, key, value):
        if key in self.od: self.od.move_to_end(key)
        self.od[key]=value
        if len(self.od)>self.c: self.od.popitem(last=False)