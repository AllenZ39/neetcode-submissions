import codecs


class Solution:
    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += str(len(s)) + "π" + s
        print(e)
        return e

    def decode(self, s: str) -> List[str]:
        d = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "π":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            d.append(s[i:j])
            i = j
        return d
