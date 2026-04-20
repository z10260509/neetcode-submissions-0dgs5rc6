class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        length = 0
        res = 1

        if not nums:
            return 0

        curr = nums[0]
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                length = 0
                curr = nums[i]
            while i< len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            curr += 1
            length += 1
            i+=1
            res = max(res, length)
        


        return res