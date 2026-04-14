class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            length = 0
            while i:
                i &= (i-1)
                length += 1
            res.append(length)

        return res