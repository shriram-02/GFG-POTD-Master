class Solution:
    def maxPeopleDefeated(self, p):
        lo, hi = 0, 10000
        
        while lo <= hi:
            mid = (lo + hi) // 2
            s = mid * (mid + 1) * (2 * mid + 1) // 6
            
            if s <= p:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi