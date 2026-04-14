class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        exist = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            exist[s[i]] += 1
            exist[t[i]] -= 1

        for x in exist:
            if exist[x]:
                return False
        
        return True