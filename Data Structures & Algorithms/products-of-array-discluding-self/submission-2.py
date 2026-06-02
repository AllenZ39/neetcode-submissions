class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = []
        p = 1
        z = 0
        for i, num in enumerate(nums):
            if num != 0:
                p *= num
            else:
                if z == 1:
                    return [0] * len(nums)
                z += 1

        for i, num in enumerate(nums):
            if num != 0:
                m.append(p // num)
            else:
                m = [0] * len(nums)
                m[i] = p
                return m
        return m
