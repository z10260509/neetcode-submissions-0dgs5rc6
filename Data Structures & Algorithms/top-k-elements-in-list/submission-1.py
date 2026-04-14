class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        arr = []

        for num in count.keys():
            arr.append([count[num], num])
        arr.sort()
        
        res = []

        for i in range(k):
            res.append(arr.pop()[1])
        return res