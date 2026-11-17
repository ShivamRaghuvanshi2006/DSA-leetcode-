class Solution:
    def getImportance(self, employees, id):
        mp = {e.id: e for e in employees}
        def dfs(i):
            e = mp[i]
            return e.importance + sum(dfs(s) for s in e.subordinates)
        return dfs(id)
