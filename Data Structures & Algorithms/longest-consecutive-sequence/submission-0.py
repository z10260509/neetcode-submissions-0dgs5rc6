class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in nums:
            if num-1 not in numset:
                length = 0
                while num in numset:
                    num += 1
                    length += 1
                res = max(res, length)
        
        return res