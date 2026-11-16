class Solution:
    def cloneGraph(self, node):
        from collections import deque
        if not node: return None
        mp={node.val:Node(node.val)}
        q=deque([node])
        while q:
            cur=q.popleft()
            for nb in cur.neighbors:
                if nb.val not in mp:
                    mp[nb.val]=Node(nb.val); q.append(nb)
                mp[cur.val].neighbors.append(mp[nb.val])
        return mp[node.val]