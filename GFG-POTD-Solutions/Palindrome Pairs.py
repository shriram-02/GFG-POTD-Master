class Solution:
    def palindromePair(self, arr):
        
        def isPalindrome(s):
            return s == s[::-1]
        
        mp = {}
        
        for i, word in enumerate(arr):
            mp[word] = i
        
        for i, word in enumerate(arr):
            n = len(word)
            
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                
                # Case 1
                if isPalindrome(left):
                    rev = right[::-1]
                    
                    if rev in mp and mp[rev] != i:
                        return True
                
                # Case 2
                if j != n and isPalindrome(right):
                    rev = left[::-1]
                    
                    if rev in mp and mp[rev] != i:
                        return True
        
        return False