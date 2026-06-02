class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = defaultdict(list)
        for word in strs:
            dt = [0] * 26
            for char in word:
                dt[ord(char) - ord("a")] += 1
            hashm[tuple(dt)].append(word)

        return list(hashm.values())
