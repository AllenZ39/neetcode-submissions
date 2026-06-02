class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = []
        p = 1
        z = False
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                p *= num
            else:
                if z:
                    return [0 for num in nums]
                z = True
                j = i
        if z:
            for i, num in enumerate(nums):
                if i != j:
                    m.append(0)
                else:
                    m.append(p)
            return m
        for num in nums:
            if num != 0:
                m.append(int(p / num))
            else:
                m.append(0)
        return m
