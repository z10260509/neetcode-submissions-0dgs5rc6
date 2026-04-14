class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for x in strs:
            count_single = defaultdict(int)

            for y in x:
                count_single[y] += 1
            
            count[tuple(sorted(count_single.items()))].append(x)

        return list(count.values())