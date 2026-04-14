class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        length = 0
        count = defaultdict(int)
        
        for r in range(len(s)):
        
            count[s[r]] += 1
            length += 1

            while count[s[r]] > 1:
                length -= 1
                count[s[l]] -= 1
                l += 1

            res = max(length, res)
        
        return res