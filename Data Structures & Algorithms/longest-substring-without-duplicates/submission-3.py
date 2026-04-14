class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        count = {}
        
        for r in range(len(s)):
            
            if s[r] in count and count[s[r]] >= l:
                l = count[s[r]] + 1
            
            count[s[r]] = r
            res = max(r - l + 1, res)

        
        return res