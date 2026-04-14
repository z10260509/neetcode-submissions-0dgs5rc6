class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def twosum(twonums: List[int], start: int, target: int) -> set():
            count = set()
            n = len(twonums)
            res = set()
            
            for i in range(start, n):
                need = target - twonums[i]
                if need in count:
                    res.add(tuple(sorted([need, twonums[i]])))
                count.add(twonums[i])
                
            return res
        
        n = len(nums)
        for i in range(n):
            pair = twosum(nums, i+1, -nums[i])

            for j in pair:
                ans.add(tuple(sorted([nums[i], j[0], j[1]])))
        return [list(t) for t in ans]

        
                



         