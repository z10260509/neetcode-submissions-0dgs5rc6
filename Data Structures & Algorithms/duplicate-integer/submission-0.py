class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = defaultdict(int)

        for x in nums:
            if exist[x] >= 1:
                return True
            exist[x] += 1

        return False