import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        hashm = {}
        d = {}
        for letter in string.ascii_lowercase:
            d[letter] = 0
        for word in strs:
            dt = d.copy()
            for char in word:
                dt[char] += 1
            t = tuple(dt.items())
            if t in hashm:
                hashm[t].append(word)
            else:
                hashm[t] = [word]
        
        for anagrams in hashm.values():
            solution.append(anagrams)
        return solution
        