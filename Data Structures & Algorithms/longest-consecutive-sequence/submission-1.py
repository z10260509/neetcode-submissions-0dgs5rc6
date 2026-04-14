class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        length = defaultdict(int)

        for num in nums:
            if not length[num]:
                length[num] = length[num-1] + length[num+1] + 1
                length[num - length[num-1]] = length[num]
                length[num + length[num+1]] = length[num]
                res = max(res, length[num])


        return res