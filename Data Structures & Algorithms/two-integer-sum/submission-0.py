class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = defaultdict(int)

        for i in range(len(nums)):
            remain[nums[i]] = i

        for j in range(len(nums)):
            if target - nums[j] in remain and remain[target - nums[j]] != j:
                return [j, remain[target - nums[j]]]

        return []