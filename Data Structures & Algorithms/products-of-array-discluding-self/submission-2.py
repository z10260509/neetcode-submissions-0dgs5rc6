class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix, postfix = 1, 1

        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
 