class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix , postfix = [1] * (n+1), [1] * (n+1)
        prefix[0] = 1
        postfix[0] = 1
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[i] = postfix[i-1] * nums[-i]

        res = []

        for i in range(n):
            res.append(prefix[i] * postfix[n - i -1])

        return res
