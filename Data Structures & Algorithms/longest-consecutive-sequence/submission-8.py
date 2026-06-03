class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for num in nums:
            if num not in mp:
                left = mp.get(num - 1, 0)
                right = mp.get(num + 1, 0)
                
                length = left + right + 1
                mp[num] = length
                res = max(res, length)
                
                mp[num - left] = length
                mp[num + right] = length
        return res
