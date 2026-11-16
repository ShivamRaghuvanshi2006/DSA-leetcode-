class Solution:
    def pathSum(self, root, targetSum):
        res=[]
        def dfs(n,rem,path):
            if not n: return
            path.append(n.val)
            if not n.left and not n.right and n.val==rem:
                res.append(list(path))
            else:
                dfs(n.left,rem-n.val,path)
                dfs(n.right,rem-n.val,path)
            path.pop()
        dfs(root,targetSum,[])
        return res