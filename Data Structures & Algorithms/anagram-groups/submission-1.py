class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for x in strs:
            count_single = [0] * 26

            for y in x:
                count_single[ord(y) - ord('a')] += 1
            
            count[tuple(count_single)].append(x)

        return list(count.values())