class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        length = 1
        res = 1

        if not nums:
            return 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] != nums[i+1] - 1:
                length = 1
            else:
                length += 1
                res = max(res, length)
        


        return res