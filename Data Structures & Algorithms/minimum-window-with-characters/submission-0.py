class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = defaultdict(int)
        
        for c in t:
            count[c] += 1
        
        window = defaultdict(int)
        have = 0
        need = len(count)
        res = [-1, -1]
        length = float('infinity')
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < length:
                    length = r -l + 1
                    res = [l, r]
                
                window[s[l]] -= 1

                if window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[res[0]: res[1] + 1] if res != float('infinity') else ""
