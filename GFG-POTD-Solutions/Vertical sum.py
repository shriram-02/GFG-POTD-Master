from collections import defaultdict, deque

class Solution:
    def verticalSum(self, root):
        mp = defaultdict(int)
        
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            
            mp[hd] += node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        res = []
        
        for key in sorted(mp):
            res.append(mp[key])
        
        return res