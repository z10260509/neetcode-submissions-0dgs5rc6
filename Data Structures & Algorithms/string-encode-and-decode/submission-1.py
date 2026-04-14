class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += ','
        res += '|'

        for s in strs:
            res += s

        return res


    def decode(self, s: str) -> List[str]:
        size, res = [], []
        i = 0
        while s[i] != '|':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            size.append(int(cur))
            i += 1
        i += 1
        for sz in size:
            res.append(s[i:i+sz])
            i += sz
        return res