class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
       
        for x in nums:
            count[x] += 1

        res = []
        n = len(nums)

        for i in range(n):
            count[nums[i]] -= 1

            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, n):
                count[nums[j]] -= 1

                if j-1 > i and nums[j] == nums[j - 1]:
                    continue

                if count[-(nums[i] + nums[j])] > 0:
                    res.append([nums[i], nums[j], -(nums[i] + nums[j])])

            for j in range(i+1, n):
                count[nums[j]] += 1

        return res    
