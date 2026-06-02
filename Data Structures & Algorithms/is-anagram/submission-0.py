class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for c in s:
            ds[c] = ds.setdefault(c, 0) + 1
        for c in t:
            dt[c] = dt.setdefault(c, 0) + 1
        for k in ds.keys():
            if ds[k] != dt.get(k, 0):
                return False
        return True