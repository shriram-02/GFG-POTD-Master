class Solution:
    def validGroups(self, s):
        n = len(s)
        
        # Prefix sum of digits
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + int(s[i])
        
        dp = {}
        
        def solve(idx, prev_sum):
            if idx == n:
                return 1
            
            if (idx, prev_sum) in dp:
                return dp[(idx, prev_sum)]
            
            ans = 0
            
            for j in range(idx, n):
                curr_sum = prefix[j + 1] - prefix[idx]
                
                if curr_sum >= prev_sum:
                    ans += solve(j + 1, curr_sum)
            
            dp[(idx, prev_sum)] = ans
            
            return ans
        
        return solve(0, 0)